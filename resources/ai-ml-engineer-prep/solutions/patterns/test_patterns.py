"""Tests for the 17 extra coding patterns. Run: python3 test_patterns.py"""
import itertools
import math
import random

from attention import attention
from backoff import backoff_delay, retry
from classification_metrics import confusion, precision_recall_f1, roc_auc
from kmeans import inertia, kmeans
from logistic_regression import fit, log_loss, predict_proba
from transformer_params import llama_params
from bpe_merge import bpe_step, merge_pair, most_frequent_pair
from chunker import chunk_tokens, chunk_words
from kv_cache import GB, GiB, kv_bytes_per_token, kv_cache_bytes, max_tokens_in_cache, weight_bytes
from logsumexp import log_softmax, logsumexp
from lru_cache import LRUCache, PrefixCache
from mmr import mmr
from mrr import mean_reciprocal_rank, reciprocal_rank
from ndcg import dcg, ndcg_at_k
from rrf import rrf
from softmax import softmax
from sse_parser import SSEParser
from token_bucket import TokenBucket
from top_k_sampling import sample_top_k, top_k_probs
from top_p_sampling import sample_top_p, top_p_probs
from trimmer import trim_history

PASSED = []


def case(fn):
    fn()
    PASSED.append(fn.__name__)
    return fn


def close(a, b, tol=1e-9):
    return abs(a - b) <= tol


@case
def test_softmax():
    p = softmax([2.0, 1.0, 0.0])
    assert close(sum(p), 1.0)
    assert close(p[0], math.exp(2) / (math.exp(2) + math.exp(1) + 1))
    assert [round(x, 4) for x in p] == [0.6652, 0.2447, 0.09]
    # stability: huge logits would overflow math.exp without the max shift
    assert close(softmax([1000.0, 1000.0])[0], 0.5)
    # temperature: T < 1 sharpens, T > 1 flattens, T -> large is uniform
    assert softmax([2.0, 1.0, 0.0], 0.5)[0] > p[0] > softmax([2.0, 1.0, 0.0], 2.0)[0]
    assert [round(x, 4) for x in softmax([2.0, 1.0, 0.0], 0.5)] == [0.8668, 0.1173, 0.0159]
    assert softmax([]) == []
    try:
        softmax([1.0], 0)
        raise AssertionError
    except ValueError:
        pass


@case
def test_logsumexp():
    assert close(logsumexp([0.0, 0.0]), math.log(2))
    assert close(logsumexp([1000.0, 1000.0]), 1000 + math.log(2))
    assert logsumexp([]) == -math.inf
    assert logsumexp([-math.inf, -math.inf]) == -math.inf
    ls = log_softmax([2.0, 1.0, 0.0])
    assert close(sum(math.exp(x) for x in ls), 1.0)
    # log_softmax stays finite where log(softmax) underflows to log(0)
    assert log_softmax([0.0, -2000.0])[1] == -2000.0


@case
def test_top_k():
    probs = top_k_probs([1.0, 3.0, 2.0, 3.0], 2)
    assert probs[0] == 0 and probs[2] == 0 and close(probs[1], 0.5) and close(probs[3], 0.5)
    probs = top_k_probs([0.0, 1.0, 2.0], 2)
    assert probs[0] == 0.0 and close(probs[2], math.e / (math.e + 1))
    rng = random.Random(0)
    counts = [0, 0, 0]
    for _ in range(20000):
        counts[sample_top_k([0.0, 1.0, 2.0], 2, rng=rng)] += 1
    assert counts[0] == 0 and abs(counts[2] / 20000 - 0.7311) < 0.02
    assert sample_top_k([0.0, 5.0, 5.0], 1, temperature=0) == 1   # greedy, tie -> smaller index


@case
def test_top_p():
    # probs 0.5, 0.3, 0.15, 0.05 (logits are their logs)
    lg = [math.log(x) for x in [0.5, 0.3, 0.15, 0.05]]
    p = top_p_probs(lg, 0.75)
    assert close(p[0], 0.5 / 0.8) and close(p[1], 0.3 / 0.8) and p[2] == 0 and p[3] == 0
    p = top_p_probs(lg, 0.8)                 # 0.5 + 0.3 = 0.8 reaches p exactly
    assert p[2] == 0 and close(p[0] + p[1], 1.0)
    p = top_p_probs(lg, 0.1)                 # at least one token always survives
    assert p == [1.0, 0.0, 0.0, 0.0]
    assert top_p_probs(lg, 1.0)[3] > 0
    rng = random.Random(1)
    assert all(sample_top_p(lg, 0.75, rng=rng) in (0, 1) for _ in range(2000))


@case
def test_cosine_topk():
    try:
        import numpy as np
    except ImportError:
        print("  (numpy not installed: cosine_top_k skipped)")
        return
    from cosine_topk import cosine_top_k
    m = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 0.0], [2.0, 0.0]])
    idx, sc = cosine_top_k(m, np.array([1.0, 0.0]), 3)
    assert list(idx) == [0, 4, 2]            # 0 and 4 tie at 1.0 -> smaller index first
    assert close(sc[2], 1 / math.sqrt(2))
    idx, sc = cosine_top_k(m, np.array([0.0, 0.0]), 2)
    assert list(idx) == [0, 1] and list(sc) == [0.0, 0.0]   # zero query: all 0, no NaN
    rng = np.random.default_rng(0)
    m = rng.integers(-2, 3, size=(300, 4)).astype(float)    # many exact ties
    q = rng.integers(-2, 3, size=4).astype(float)
    idx, _ = cosine_top_k(m, q, 25)
    norms = np.linalg.norm(m, axis=1) * np.linalg.norm(q)
    full = [(-(m[i] @ q / norms[i]) if norms[i] > 0 else 0.0, i) for i in range(300)]
    assert list(idx) == [i for _, i in sorted(full)[:25]]


@case
def test_rrf():
    bm25 = ["d1", "d2", "d3"]
    dense = ["d3", "d1", "d4"]
    out = rrf([bm25, dense])
    s = dict(out)
    assert close(s["d1"], 1 / 61 + 1 / 62) and close(s["d3"], 1 / 63 + 1 / 61)
    assert close(s["d2"], 1 / 62) and close(s["d4"], 1 / 63)
    assert [d for d, _ in out] == ["d1", "d3", "d2", "d4"]
    assert rrf([["a", "a", "b"]]) == [("a", 1 / 61), ("b", 1 / 63)]   # duplicate keeps first position
    assert rrf([], k=60) == []
    assert rrf([["x", "y"]], top_n=1) == [("x", 1 / 61)]


@case
def test_ndcg():
    rel = {"a": 3, "b": 2, "c": 1}
    assert close(ndcg_at_k(["a", "b", "c"], rel, 3), 1.0)
    got = ndcg_at_k(["c", "b", "a"], rel, 3)
    d = 1 + 2 / math.log2(3) + 3 / 2
    i = 3 + 2 / math.log2(3) + 1 / 2
    assert close(got, d / i)
    assert round(got, 6) == 0.789998
    # missing a relevant doc is penalized because the ideal uses ALL judged docs
    assert ndcg_at_k(["a", "x"], rel, 2) < 1.0
    assert ndcg_at_k(["x"], {}, 5) == 0.0
    assert close(dcg([1, 1]), 1 + 1 / math.log2(3))
    assert ndcg_at_k(["c", "b", "a"], rel, 3, exponential=True) < got   # bigger penalty for burying the 3


@case
def test_mrr():
    assert reciprocal_rank(["x", "a", "b"], {"a", "b"}) == 0.5
    assert reciprocal_rank(["x", "y"], {"a"}) == 0.0
    assert reciprocal_rank(["x", "y", "a"], {"a"}, k=2) == 0.0
    assert close(mean_reciprocal_rank([["a"], ["x", "a"], ["x", "y"]], [{"a"}, {"a"}, {"a"}]), (1 + 0.5 + 0) / 3)


@case
def test_mmr():
    q = [0.9, 0.88, 0.5]
    sims = [[1, 0.99, 0.1], [0.99, 1, 0.1], [0.1, 0.1, 1]]
    assert mmr(q, sims, 2, lam=1.0) == [0, 1]       # pure relevance takes the near-duplicate
    assert mmr(q, sims, 2, lam=0.5) == [0, 2]       # diversity skips it
    assert mmr(q, sims, 3, lam=0.5) == [0, 2, 1]
    assert mmr([], [], 3) == []
    assert mmr([0.5, 0.5], [[1, 0], [0, 1]], 1) == [0]


@case
def test_token_bucket():
    t = [0.0]
    tb = TokenBucket(rate=2.0, capacity=5, clock=lambda: t[0])
    assert all(tb.allow() for _ in range(5)) and not tb.allow()   # burst of 5, then empty
    t[0] = 0.5
    assert tb.allow() and not tb.allow()                         # 0.5 s * 2/s = 1 token
    t[0] = 100.0
    assert close(tb.wait_time(5), 0.0) and tb.allow(5)            # capped at capacity, not 200
    assert close(tb.wait_time(1), 0.5)
    assert tb.wait_time(6) == float("inf")


@case
def test_lru_and_prefix_cache():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") == 1                    # a is now most recent
    assert c.put("c", 3) == "b"               # so b is evicted
    assert c.get("b") is None and c.get("c") == 3
    pc = PrefixCache(block=4, capacity_blocks=100)
    system = list(range(12))
    pc.insert(system + [100, 101, 102, 103])
    assert pc.lookup(system + [200, 201, 202, 203]) == 12      # shared prefix reused
    assert pc.lookup([999] + system[1:] + [100, 101, 102, 103]) == 0   # first token changed: nothing reused
    assert pc.lookup(system[:6]) == 4                          # only full blocks count


@case
def test_bpe():
    vocab = {tuple("low"): 5, tuple("lower"): 2, tuple("newest"): 6, tuple("widest"): 3}
    pair = most_frequent_pair(vocab)
    assert pair == ("e", "s")                 # es: 6 + 3 = 9, st: 9 too, ties -> smallest pair
    pair, v2 = bpe_step(vocab)
    assert v2[("n", "e", "w", "es", "t")] == 6 and v2[("l", "o", "w")] == 5
    pair, v3 = bpe_step(v2)
    assert pair == ("es", "t")
    assert merge_pair({("a", "a", "a"): 1}, ("a", "a")) == {("aa", "a"): 1}   # non-overlapping, left to right
    assert bpe_step({("x",): 3}) == (None, {("x",): 3})


@case
def test_kv_cache():
    b = kv_cache_bytes(32, 8, 128, 8192, 4, 2)
    assert b == 4 * GiB                       # the assessment question: 4 GiB
    assert kv_bytes_per_token(32, 8, 128, 2) == 131072           # 128 KiB per token
    assert kv_bytes_per_token(32, 32, 128, 2) == 524288          # MHA (32 KV heads): 4x more
    assert weight_bytes(8e9, "bf16") / GB == 16.0
    assert weight_bytes(70e9, "int4") / GB == 35.0
    assert max_tokens_in_cache(10 * GiB, 32, 8, 128, 2) == 81920


@case
def test_backoff():
    rng = random.Random(0)
    for attempt in range(10):
        d = backoff_delay(attempt, base=0.5, cap=8.0, rng=rng)
        assert 0 <= d <= min(8.0, 0.5 * 2 ** attempt)
    calls, sleeps = [0], []

    def flaky():
        calls[0] += 1
        if calls[0] < 3:
            raise TimeoutError
        return "ok"

    assert retry(flaky, sleep=sleeps.append, rng=random.Random(1)) == "ok"
    assert calls[0] == 3 and len(sleeps) == 2
    try:
        retry(lambda: (_ for _ in ()).throw(ValueError("bad input")), sleep=sleeps.append)
        raise AssertionError
    except ValueError:
        pass                                  # non-retryable errors propagate immediately
    try:
        retry(lambda: (_ for _ in ()).throw(TimeoutError()), max_attempts=3, sleep=lambda s: None)
        raise AssertionError
    except TimeoutError:
        pass


@case
def test_chunker():
    toks = list(range(10))
    assert chunk_tokens(toks, 4, 1) == [[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9]]
    assert chunk_tokens(toks, 4, 2) == [[0, 1, 2, 3], [2, 3, 4, 5], [4, 5, 6, 7], [6, 7, 8, 9]]
    assert chunk_tokens(toks, 20, 5) == [toks]
    assert chunk_tokens([], 4, 1) == []
    for n, size, ov in itertools.product(range(1, 40), range(1, 9), range(0, 8)):
        if ov >= size:
            continue
        out = chunk_tokens(list(range(n)), size, ov)
        assert out[0][0] == 0 and out[-1][-1] == n - 1
        expected = 1 if n <= size else 1 + math.ceil((n - size) / (size - ov))
        assert len(out) == expected
    assert chunk_words("a b c d e", 2, 0) == ["a b", "c d", "e"]
    try:
        chunk_tokens(toks, 4, 4)
        raise AssertionError
    except ValueError:
        pass


@case
def test_sse():
    stream = ('data: {"delta": "Hel"}\n\n: keep-alive\n\nevent: done\r\ndata: line1\r\ndata:line2\r\nid: 7\r\n\r\n'
              'data: x\r\rdata: y\n\n')
    expected = [
        {"event": "message", "data": '{"delta": "Hel"}', "id": ""},
        {"event": "done", "data": "line1\nline2", "id": "7"},
        {"event": "message", "data": "x", "id": "7"},
        {"event": "message", "data": "y", "id": "7"},
    ]
    p = SSEParser()
    assert p.feed(stream) == expected
    for i in range(len(stream) + 1):          # every single split point, including between \r and \n
        p = SSEParser()
        assert p.feed(stream[:i]) + p.feed("") + p.feed(stream[i:]) == expected
    p = SSEParser()
    assert sum((p.feed(ch) for ch in stream), []) == expected   # one char at a time


@case
def test_trimmer():
    count = lambda s: len(s.split())
    msgs = [
        {"role": "system", "content": "be brief"},              # 2
        {"role": "user", "content": "one two three"},           # 3
        {"role": "assistant", "content": "four five"},          # 2
        {"role": "user", "content": "six seven eight nine"},    # 4
    ]
    assert trim_history(msgs, 100, count) == msgs
    assert trim_history(msgs, 8, count) == [msgs[0], msgs[2], msgs[3]]
    assert trim_history(msgs, 7, count) == [msgs[0], msgs[3]]   # assistant msg would need 8
    try:
        trim_history(msgs, 5, count)
        raise AssertionError
    except ValueError:
        pass


@case
def test_attention():
    out = attention([[1, 0]], [[1, 0], [0, 1], [1, 1]], [[1, 0], [0, 1], [1, 1]])
    assert [round(x, 4) for x in out[0]] == [0.8022, 0.5989]
    X = [[0.5, -1.0], [2.0, 0.0], [1.0, 1.0]]
    causal = attention(X, X, [[1, 0], [0, 1], [5, 5]], causal=True)
    assert causal[0] == [1.0, 0.0]                           # token 0 can only see itself
    assert max(causal[1]) <= 1.0                             # token 1 never sees the [5, 5] value of token 2
    try:
        import numpy as np
    except ImportError:
        return
    rng = np.random.default_rng(0)
    for _ in range(20):
        n, dk, dv = rng.integers(1, 6), rng.integers(1, 5), rng.integers(1, 4)
        Q, K, V = rng.normal(size=(n, dk)), rng.normal(size=(n, dk)), rng.normal(size=(n, dv))
        s_ = Q @ K.T / np.sqrt(dk)
        s_ = s_ + np.triu(np.full((n, n), -np.inf), 1)
        w = np.exp(s_ - s_.max(axis=1, keepdims=True))
        ref = (w / w.sum(axis=1, keepdims=True)) @ V
        got = np.array(attention(Q.tolist(), K.tolist(), V.tolist(), causal=True))
        assert np.allclose(got, ref)


@case
def test_transformer_params():
    assert llama_params(32000, 4096, 32, 11008, 32, 32) == 6738415616      # Llama 2 7B
    assert llama_params(128256, 4096, 32, 14336, 32, 8) == 8030261248      # Llama 3 8B
    assert llama_params(32000, 4096, 32, 11008, 32, 32, tied_embeddings=True) == 6738415616 - 32000 * 4096


@case
def test_classification_metrics():
    y = [1] * 60 + [0] * 940
    pred = [1] * 40 + [0] * 20 + [1] * 10 + [0] * 930
    assert confusion(y, pred) == {"tp": 40, "fp": 10, "fn": 20, "tn": 930}
    p, r, f = precision_recall_f1(y, pred)
    assert close(p, 0.8) and close(r, 2 / 3) and round(f, 4) == 0.7273
    assert precision_recall_f1([1, 0], [0, 0]) == (0.0, 0.0, 0.0)       # no positive predictions
    assert round(roc_auc([1, 1, 1, 0, 0, 0, 0], [0.9, 0.8, 0.4, 0.7, 0.3, 0.2, 0.1]), 4) == 0.9167
    assert roc_auc([1, 0], [0.5, 0.5]) == 0.5                           # tie counts half
    rng = random.Random(4)
    for _ in range(300):
        n = rng.randint(2, 12)
        yt = [rng.randint(0, 1) for _ in range(n)]
        if len(set(yt)) < 2:
            continue
        sc = [rng.choice([0.1, 0.2, 0.5, 0.7, 0.9]) for _ in range(n)]   # many ties
        pos = [s for s, t in zip(sc, yt) if t]
        neg = [s for s, t in zip(sc, yt) if not t]
        brute = sum(1 if a > b else 0.5 if a == b else 0 for a in pos for b in neg) / (len(pos) * len(neg))
        assert close(roc_auc(yt, sc), brute)


@case
def test_logistic_regression():
    X = [[0.0, 0.0], [1.0, 0.5], [0.5, 1.0], [3.0, 3.0], [4.0, 3.5], [3.5, 4.0]]
    y = [0, 0, 0, 1, 1, 1]
    w, b = fit(X, y, lr=0.5, epochs=300)
    assert [round(pr) for pr in predict_proba(X, w, b)] == y
    assert log_loss(X, y, w, b) < log_loss(X, y, [0.0, 0.0], 0.0)
    # gradient check: analytic gradient of one GD step matches finite differences
    w0, b0, h = [0.3, -0.2], 0.1, 1e-6
    from logistic_regression import sigmoid
    gw = [sum((sigmoid(w0[0] * xi[0] + w0[1] * xi[1] + b0) - yi) * xi[j] for xi, yi in zip(X, y)) / 6 for j in range(2)]
    for j in range(2):
        wp = list(w0); wp[j] += h
        wm = list(w0); wm[j] -= h
        num = (log_loss(X, y, wp, b0) - log_loss(X, y, wm, b0)) / (2 * h)
        assert abs(num - gw[j]) < 1e-6


@case
def test_kmeans():
    rng = random.Random(0)
    blobs = [(0, 0), (10, 10), (0, 10)]
    pts = [(cx + rng.gauss(0, 0.5), cy + rng.gauss(0, 0.5)) for cx, cy in blobs for _ in range(30)]
    cents, assign = kmeans(pts, 3, seed=1)
    for b in range(3):                                   # each blob lands in exactly one cluster
        assert len(set(assign[b * 30:(b + 1) * 30])) == 1
    assert len(set(assign)) == 3
    assert inertia(pts, cents, assign) < 3 * 90 * 0.5 ** 2 * 2
    one = kmeans([(1.0, 2.0)] * 4, 1)
    assert one[0] == [[1.0, 2.0]] and one[1] == [0, 0, 0, 0]


if __name__ == "__main__":
    print(f"patterns: all {len(PASSED)} pattern test groups passed")
