"""Tests for extractObjects and StreamingExtractor: examples, escape edge
cases, every possible split point, randomized generated streams with known
answers, a 200,000-char timing check, and the variants."""
import json
import random
import time

from extract_objects import Solution, StreamingExtractor
from extract_objects_variants import extract_spans, extract_valid, extract_values

WEATHER = [
    'Calling tools now {"tool": "get_weather", "args": {"city": "Chen',
    'nai", "unit": "C"}} then {"tool": "search", "args": {"q": "a } b"',
    '}} done',
]
WEATHER_OUT = [
    '{"tool": "get_weather", "args": {"city": "Chennai", "unit": "C"}}',
    '{"tool": "search", "args": {"q": "a } b"}}',
]


def stream_all(chunks):
    ex = StreamingExtractor()
    out = []
    for c in chunks:
        out.extend(ex.feed(c))
    return out


def test_examples():
    s = Solution()
    assert s.extractObjects(WEATHER) == WEATHER_OUT
    assert stream_all(WEATHER) == WEATHER_OUT
    assert s.extractObjects(['{"note": "unfinished"']) == []
    assert stream_all(['{"note": "unfinished"']) == []


def test_escapes():
    s = Solution()
    # \" does not end the string, so the } inside is still string content
    assert s.extractObjects(['{"a": "x\\"}"}']) == ['{"a": "x\\"}"}']
    # \\ is an escaped backslash; the next " DOES end the string
    assert s.extractObjects(['{"a": "x\\\\"}']) == ['{"a": "x\\\\"}']
    # split between the backslash and the char it escapes
    chunks = ['{"a": "q\\', '"}', '"}']
    assert s.extractObjects(chunks) == ['{"a": "q\\"}"}']
    assert stream_all(chunks) == ['{"a": "q\\"}"}']
    # braces and quotes outside any object are ignored
    # the { starts an object, the next " opens a string that swallows the }, never closed
    assert s.extractObjects(['}} "{" }']) == []
    assert s.extractObjects(['} ] "x" {}']) == ['{}']
    assert s.extractObjects(['{}{}', '{{}}']) == ['{}', '{}', '{{}}']
    assert s.extractObjects([]) == []
    assert s.extractObjects(['', '', '']) == []


def test_every_split_point():
    text = "".join(WEATHER) + ' {"k": "\\\\\\"}{"} tail {"open": '
    expected = Solution().extractObjects([text])
    assert expected == WEATHER_OUT + ['{"k": "\\\\\\"}{"}']
    for i in range(len(text) + 1):
        for j in range(i, len(text) + 1, 7):
            parts = [text[:i], text[i:j], text[j:]]
            assert Solution().extractObjects(parts) == expected
            assert stream_all(parts) == expected


def random_value(rng, depth=0):
    r = rng.random()
    if depth > 3 or r < 0.3:
        return "".join(rng.choice('ab{}[]"\\:, \n\t') for _ in range(rng.randint(0, 6)))
    if r < 0.45:
        return rng.randint(-5, 500)
    if r < 0.55:
        return [random_value(rng, depth + 1) for _ in range(rng.randint(0, 3))]
    return {random_value(rng, 9): random_value(rng, depth + 1) for _ in range(rng.randint(0, 3))}


def test_randomized_streams():
    rng = random.Random(42)
    s = Solution()
    for _ in range(1500):
        objs, pieces = [], []
        for _ in range(rng.randint(0, 5)):
            noise = "".join(rng.choice('xyz ]"\\:\n') for _ in range(rng.randint(0, 8)))  # no { or } in noise
            pieces.append(noise)
            obj = {str(random_value(rng, 9)): random_value(rng) for _ in range(rng.randint(0, 4))}
            text = json.dumps(obj, ensure_ascii=rng.random() < 0.5)
            objs.append(text)
            pieces.append(text)
        if rng.random() < 0.5:
            pieces.append('{"tail": "never closed ' + rng.choice(["", "\\", "}", '\\"}']))
        stream = "".join(pieces)
        cuts = sorted(rng.sample(range(len(stream) + 1), min(len(stream) + 1, rng.randint(0, 12))))
        chunks, prev = [], 0
        for c in cuts:
            chunks.append(stream[prev:c])
            prev = c
        chunks.append(stream[prev:])
        assert s.extractObjects(chunks) == objs
        assert stream_all(chunks) == objs
        assert [json.loads(o) for o in objs] == extract_valid(chunks)


def test_performance():
    obj = json.dumps({"tool": "search", "args": {"q": "a } b \\\" {", "n": [1, 2, {"x": "}"}]}})
    stream = ("noise " + obj) * (200_000 // (len(obj) + 6))
    chunks = [stream[i:i + 37] for i in range(0, len(stream), 37)]
    t0 = time.perf_counter()
    out = Solution().extractObjects(chunks)
    dt = time.perf_counter() - t0
    assert len(stream) <= 200_000 and len(out) == stream.count("noise ")
    t1 = time.perf_counter()
    assert stream_all(chunks) == out
    dt2 = time.perf_counter() - t1
    assert dt < 1.0 and dt2 < 1.0
    return len(stream), dt, dt2


def test_variants():
    assert extract_valid(['{"a": 1} {"b": } {"c": [1, 2]}']) == [{"a": 1}, {"c": [1, 2]}]
    assert extract_values(['x [1, {"a": "]"}] y {"b": [2]} [}] z']) == ['[1, {"a": "]"}]', '{"b": [2]}']
    text = 'pre {"a": 1} mid {"b": "}"} post'
    spans = extract_spans([text])
    assert [text[a:b] for a, b in spans] == ['{"a": 1}', '{"b": "}"}']


if __name__ == "__main__":
    test_examples()
    test_escapes()
    test_every_split_point()
    test_randomized_streams()
    n, dt, dt2 = test_performance()
    test_variants()
    print(f"extract_objects: all tests passed (every split point, 1500 randomized streams; {n} chars in {dt*1000:.0f} ms joined, {dt2*1000:.0f} ms streaming)")
