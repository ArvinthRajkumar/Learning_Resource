"""Every number quoted in the guide, computed and asserted.

Run:  python3 verify_numbers.py        (prints each computation)
The pages quote these exact values; if a value here changes, the page is wrong.
"""
import math
from fractions import Fraction

GiB, MiB, KiB, GB = 1024 ** 3, 1024 ** 2, 1024, 1000 ** 3
OUT = []


def show(label, value, expect=None, tol=1e-9):
    OUT.append(f"  {label} = {value}")
    if expect is not None:
        ok = (abs(value - expect) <= tol) if isinstance(value, float) or isinstance(expect, float) else value == expect
        assert ok, f"{label}: got {value}, expected {expect}"


def kv(layers, kv_heads, head_dim, seq, batch, nbytes):
    return 2 * layers * kv_heads * head_dim * seq * batch * nbytes


def page01():
    OUT.append("[01] Inference and memory")
    b = kv(32, 8, 128, 8192, 4, 2)
    show("KV question bytes 2*32*8*128*8192*4*2", b, 4294967296)
    show("  in GiB", b / GiB, 4.0)
    show("  in GB (decimal)", round(b / GB, 3), 4.295)
    show("KV per token (32 layers, 8 kv heads, dim 128, fp16) bytes", kv(32, 8, 128, 1, 1, 2), 131072)
    # wrong-option patterns for the KV question
    show("forgot the 2 (K and V) -> GiB", kv(32, 8, 128, 8192, 4, 2) / 2 / GiB, 2.0)
    show("used 32 query heads instead of 8 kv heads -> GiB", kv(32, 32, 128, 8192, 4, 2) / GiB, 16.0)
    show("used fp32 and 32 heads -> GiB", kv(32, 32, 128, 8192, 4, 4) / GiB, 32.0)
    show("one sequence only (batch 1) -> GiB", kv(32, 8, 128, 8192, 1, 2) / GiB, 1.0)
    # model configs (per published config.json files)
    show("Llama-2-7B MHA per token KiB", kv(32, 32, 128, 1, 1, 2) / KiB, 512.0)
    show("Llama-2-7B 4096 tokens GiB", kv(32, 32, 128, 4096, 1, 2) / GiB, 2.0)
    show("Llama-3-8B GQA per token KiB", kv(32, 8, 128, 1, 1, 2) / KiB, 128.0)
    show("Llama-3-8B 8192 tokens GiB", kv(32, 8, 128, 8192, 1, 2) / GiB, 1.0)
    show("Llama-2-13B MHA per token KiB", kv(40, 40, 128, 1, 1, 2) / KiB, 800.0)
    show("70B (80 layers, 8 kv heads) per token KiB", kv(80, 8, 128, 1, 1, 2) / KiB, 320.0)
    show("70B 8192 tokens GiB", kv(80, 8, 128, 8192, 1, 2) / GiB, 2.5)
    show("70B 8192 tokens x 32 users GiB", kv(80, 8, 128, 8192, 32, 2) / GiB, 80.0)
    show("70B if it were MHA (64 kv heads) per token MiB", kv(80, 64, 128, 1, 1, 2) / MiB, 2.5)
    show("8B shape MQA (1 kv head) per token KiB", kv(32, 1, 128, 1, 1, 2) / KiB, 16.0)
    show("8B shape fp8 KV cache per token KiB", kv(32, 8, 128, 1, 1, 1) / KiB, 64.0)
    # weights table
    for p in (7, 8, 13, 70):
        row = []
        for name, nb in (("fp32", 4), ("bf16", 2), ("int8", 1), ("int4", 0.5)):
            row.append(f"{name} {p * nb:g} GB / {p * 1e9 * nb / GiB:.1f} GiB")
        OUT.append(f"  {p}B: " + ", ".join(row))
    show("8B bf16 GB", 8e9 * 2 / GB, 16.0)
    show("8B bf16 GiB", round(8e9 * 2 / GiB, 2), 14.9)
    show("70B bf16 GB", 70e9 * 2 / GB, 140.0)
    show("70B int4 GB", 70e9 * 0.5 / GB, 35.0)
    # int4 with group-wise scales: one fp16 scale per 128 weights adds 16/128 bits per weight
    show("int4 + fp16 scale per group of 128: bits per weight", 4 + 16 / 128, 4.125)
    show("8B at 4.125 bits GB", round(8e9 * 4.125 / 8 / GB, 3), 4.125)
    # roofline (approximate vendor figures)
    a100_bw, a100_fl = 2.039e12, 312e12          # A100 80GB SXM: ~2.0 TB/s, 312 TFLOPS dense bf16
    h100_bw, h100_fl = 3.35e12, 989e12           # H100 SXM: ~3.35 TB/s, ~989 TFLOPS dense bf16
    show("A100 ridge point FLOP/byte", round(a100_fl / a100_bw), 153)
    show("H100 ridge point FLOP/byte", round(h100_fl / h100_bw), 295)
    show("decode batch 1 bf16 intensity FLOP/byte (2 FLOPs per 2-byte weight)", 2 / 2, 1.0)
    show("8B bf16 per-token weight read time on H100 ms", round(16e9 / h100_bw * 1e3, 2), 4.78)
    show("  -> ceiling tokens/s", round(h100_bw / 16e9), 209)
    show("8B int4 (4.125 bits) per-token time on H100 ms", round(4.125e9 / h100_bw * 1e3, 2), 1.23)
    show("  -> ceiling tokens/s", round(h100_bw / 4.125e9), 812)
    show("8B bf16 on A100 80GB ms per token", round(16e9 / a100_bw * 1e3, 2), 7.85)
    show("bytes ratio bf16 / int4 (with scales)", round(16 / 4.125, 2), 3.88)
    show("compute for 8B decode per token GFLOP (2 * params)", 2 * 8e9 / 1e9, 16.0)
    show("  time if compute bound on H100 ms", round(16e9 / h100_fl * 1e3, 4), 0.0162)
    # speculative decoding expected tokens per target pass: (1 - a^(k+1)) / (1 - a)
    def spec(a, k):
        return (1 - a ** (k + 1)) / (1 - a)
    show("spec a=0.8 k=4 tokens/pass", round(spec(0.8, 4), 4), 3.3616)
    show("spec a=0.6 k=4 tokens/pass", round(spec(0.6, 4), 4), 2.3056)
    show("spec a=0.9 k=4 tokens/pass", round(spec(0.9, 4), 4), 4.0951)
    show("spec a=0.8 k=4 with draft cost c=0.05 speedup", round(spec(0.8, 4) / (4 * 0.05 + 1), 2), 2.8)
    show("spec a=0.8 k=8", round(spec(0.8, 8), 4), 4.3289)
    # rejection sampling example: p (target), q (draft)
    p = {"A": Fraction(6, 10), "B": Fraction(3, 10), "C": Fraction(1, 10)}
    q = {"A": Fraction(3, 10), "B": Fraction(6, 10), "C": Fraction(1, 10)}
    accept = {t: min(Fraction(1), p[t] / q[t]) for t in p}
    show("accept prob if draft says A", accept["A"], Fraction(1))
    show("accept prob if draft says B", accept["B"], Fraction(1, 2))
    resid = {t: max(Fraction(0), p[t] - q[t]) for t in p}
    z = sum(resid.values())
    resid = {t: v / z for t, v in resid.items()}
    show("residual distribution on reject", (resid["A"], resid["B"], resid["C"]), (Fraction(1), Fraction(0), Fraction(0)))
    final = {t: q[t] * accept[t] + (1 - sum(q[s] * accept[s] for s in q)) * resid[t] for t in p}
    show("final distribution equals target p", final == p, True)
    show("overall acceptance rate sum min(p,q)", sum(min(p[t], q[t]) for t in p), Fraction(7, 10))
    show("Llama-2-7B 8192 tokens GiB", kv(32, 32, 128, 8192, 1, 2) / GiB, 4.0)
    show("Llama-2-13B 8192 tokens GiB", kv(40, 40, 128, 8192, 1, 2) / GiB, 6.25)
    show("6 GB of fp16 KV for Llama-3-8B, tokens", int(6e9 // kv(32, 8, 128, 1, 1, 2)), 45776)
    show("A100-40GB example: 16 users x 4096 tokens KV GiB", kv(32, 8, 128, 4096, 16, 2) / GiB, 8.0)
    show("  in GB", round(kv(32, 8, 128, 4096, 16, 2) / GB, 2), 8.59)
    show("24 GB of KV fp16 -> tokens", int(24e9 // 131072), 183105)
    show("  -> 4k sequences", int(24e9 // 131072 // 4096), 44)
    show("  fp8 -> 4k sequences", int(24e9 // 65536 // 4096), 89)
    show("  fp16 with 8k reservations -> sequences", int(24e9 // 131072 // 8192), 22)
    show("softmax(1.7, 0.9) first", round(math.exp(1.7) / (math.exp(1.7) + math.exp(0.9)), 2), 0.69)
    show("Adam mixed precision bytes/param: 2+2+4+8", 2 + 2 + 4 + 8, 16)
    # prompt caching example
    static, manual, question = 2000, 20000, 100
    show("cacheable fraction, good order", round((static + manual) / (static + manual + question), 4), 0.9955)
    # tokenization: UTF-8 bytes
    word = "வணக்கம்"
    show("Tamil 'vanakkam' code points", len(word), 7)
    show("  UTF-8 bytes", len(word.encode("utf-8")), 21)
    show("English 'hello' bytes", len("hello".encode("utf-8")), 5)
    show("bytes per Tamil code point", len("க".encode("utf-8")), 3)
    show("Tamil block U+0B80..U+0BFF all 3 bytes",
         all(len(chr(c).encode("utf-8")) == 3 for c in range(0x0B80, 0x0C00)), True)


def page02():
    OUT.append("[02] Fine-tuning")
    d, r, L = 4096, 16, 32
    per = r * (d + d)
    show("LoRA params per 4096x4096 module r=16: r*(d_in+d_out)", per, 131072)
    show("Llama-2-7B q+v, 32 layers", 2 * per * L, 8388608)
    show("  fraction of 6.74B params (%)", round(2 * per * L / 6.74e9 * 100, 3), 0.124)
    show("full delta matrix 4096x4096 params", d * d, 16777216)
    show("  LoRA compression for one module", d * d // per, 128)
    v_gqa = r * (4096 + 1024)
    show("Llama-3-8B v_proj (4096->1024) params r=16", v_gqa, 81920)
    show("Llama-3-8B q+v, 32 layers", (per + v_gqa) * L, 6815744)
    show("r=8 Llama-2-7B q+v", 8 * (d + d) * 2 * L, 4194304)
    show("all 7 linear modules Llama-2-7B r=16 (q,k,v,o 4096x4096; gate,up 4096x11008; down 11008x4096)",
         (4 * r * (4096 + 4096) + 3 * r * (4096 + 11008)) * L, 39976960)
    show("scale alpha/r for r=16, alpha=32", 32 / 16, 2.0)
    show("full FT 7B with Adam mixed precision GB (16 B/param)", 7e9 * 16 / GB, 112.0)
    show("LoRA adapter optimizer+grad+master state MB (8.39M x 16 B)", round(8388608 * 16 / 1e6), 134)
    show("QLoRA 7B base in 4-bit GB", 7e9 * 0.5 / GB, 3.5)
    # DPO worked example
    beta = 0.1
    pc, rc, pr, rr = -12.0, -14.0, -15.0, -13.0
    margin = (pc - rc) - (pr - rr)
    show("DPO margin (policy-ref chosen) - (policy-ref rejected)", margin, 4.0)
    z = beta * margin
    sig = 1 / (1 + math.exp(-z))
    show("sigmoid(beta*margin)", round(sig, 4), 0.5987)
    show("DPO loss -log sigmoid", round(-math.log(sig), 4), 0.513)
    show("DPO loss at init (policy == ref)", round(-math.log(0.5), 4), 0.6931)
    show("implicit reward chosen beta*(pc-rc)", round(beta * (pc - rc), 4), 0.2)


def page03():
    OUT.append("[03] RAG and retrieval")
    import re
    from collections import Counter
    tok = lambda t: re.findall(r"[a-z0-9]+", t.lower())
    docs = ["Cats chase mice.", "Dogs chase cats, and cats run.", "Mice eat cheese."]
    T = [tok(d) for d in docs]
    N, k1, b = 3, 1.2, 0.75
    lens = [len(t) for t in T]
    show("tiny corpus lengths", lens, [3, 6, 3])
    avgdl = sum(lens) / N
    show("avgdl", avgdl, 4.0)
    idf = lambda n: math.log(1 + (N - n + 0.5) / (n + 0.5))
    show("idf(cats), n=2", round(idf(2), 4), 0.47)
    show("idf(mice), n=2", round(idf(2), 4), 0.47)
    show("idf(cheese), n=1", round(idf(1), 4), 0.9808)
    def term(f, dl):
        return f * (k1 + 1) / (f + k1 * (1 - b + b * dl / avgdl))
    show("norm factor D1 (|D|=3): k1*(1-b+b*3/4)", round(k1 * (1 - b + b * 3 / 4), 4), 0.975)
    show("norm factor D2 (|D|=6)", round(k1 * (1 - b + b * 6 / 4), 4), 1.65)
    show("D1 tf part cats f=1", round(term(1, 3), 4), 1.1139)
    show("D2 tf part cats f=2", round(term(2, 6), 4), 1.2055)
    s1 = idf(2) * term(1, 3) + idf(2) * term(1, 3)
    s2 = idf(2) * term(2, 6)
    s3 = idf(2) * term(1, 3)
    show("score D1 (cats + mice)", round(s1, 4), 1.0471)
    show("score D2 (cats x2)", round(s2, 4), 0.5666)
    show("score D3 (mice)", round(s3, 4), 0.5235)
    show("classic idf for n=2 of N=3 (negative!)", round(math.log((3 - 2 + 0.5) / (2 + 0.5)), 4), -0.5108)
    # saturation curve points, |D| = avgdl
    show("tf curve f=1,2,5,10,100 (k1=1.2, |D|=avgdl)", [round(term(f, avgdl), 3) for f in (1, 2, 5, 10, 100)], [1.0, 1.375, 1.774, 1.964, 2.174])
    show("tf curve limit k1+1", k1 + 1, 2.2)
    # RRF example
    bm = ["D3", "D1", "D7"]
    de = ["D1", "D9", "D3"]
    sc = {}
    for lst in (bm, de):
        for r, d in enumerate(lst, 1):
            sc[d] = sc.get(d, 0) + 1 / (60 + r)
    order = sorted(sc, key=lambda d: (-sc[d], d))
    show("RRF order", order, ["D1", "D3", "D9", "D7"])
    show("RRF D1 = 1/62 + 1/61", round(sc["D1"], 6), round(1 / 62 + 1 / 61, 6))
    show("RRF D1 value", round(sc["D1"], 5), 0.03252)
    show("RRF D3 = 1/61 + 1/63", round(sc["D3"], 5), 0.03227)
    show("RRF D9 = 1/62", round(sc["D9"], 5), 0.01613)
    show("RRF D7 = 1/63", round(sc["D7"], 5), 0.01587)
    show("RRF with k=0: rank1 vs rank2 ratio", (1 / 1) / (1 / 2), 2.0)
    show("RRF with k=60: rank1 vs rank2 ratio", round((1 / 61) / (1 / 62), 4), 1.0164)
    # metrics example: retrieved d1..d5 with graded relevance; d8 relevant but not retrieved
    rel = {"d1": 3, "d3": 2, "d5": 1, "d8": 2}
    ranked = ["d1", "d2", "d3", "d4", "d5"]
    hits = [d for d in ranked if d in rel]
    show("precision@5", len(hits) / 5, 0.6)
    show("recall@5", len(hits) / len(rel), 0.75)
    show("precision@3", 2 / 3, 2 / 3)
    show("recall@3", 2 / 4, 0.5)
    show("hit rate@1 (d1 relevant)", 1, 1)
    show("RR (first relevant at 1)", 1.0, 1.0)
    ap = (1 / 1 + 2 / 3 + 3 / 5) / 4
    show("AP (divide by all 4 relevant)", round(ap, 4), 0.5667)
    dcg = 3 / math.log2(2) + 0 + 2 / math.log2(4) + 0 + 1 / math.log2(6)
    show("DCG@5", round(dcg, 4), 4.3869)
    idcg = 3 / math.log2(2) + 2 / math.log2(3) + 2 / math.log2(4) + 1 / math.log2(5)
    show("IDCG@5 (3,2,2,1)", round(idcg, 4), 5.6925)
    show("nDCG@5", round(dcg / idcg, 4), 0.7706)
    # second query for MRR / MAP
    show("MRR over q1 (RR 1) and q2 (first hit at 3)", round((1 + 1 / 3) / 2, 4), 0.6667)
    ap2 = (1 / 3) / 1
    show("MAP (q2 has one relevant doc at rank 3)", round((ap + ap2) / 2, 4), 0.45)
    # Jaccard
    A = set("the cat sat on the mat".split())
    B = set("the cat sat on a mat".split())
    show("Jaccard example |A&B|/|A|B|", (len(A & B), len(A | B)), (5, 6))
    show("  value", round(len(A & B) / len(A | B), 4), 0.8333)
    show("MinHash: P(min-hash equal) = J; std error with 128 hashes at J=0.8", round(math.sqrt(0.8 * 0.2 / 128), 4), 0.0354)
    # chunk count
    show("chunks for 10,000 tokens, size 512, overlap 64", 1 + math.ceil((10000 - 512) / (512 - 64)), 23)
    # embeddings storage
    show("1M vectors x 1536 dims x 4 bytes GB", 1_000_000 * 1536 * 4 / GB, 6.144)
    show("  fp16", 1_000_000 * 1536 * 2 / GB, 3.072)
    # cosine vs dot after normalization
    a, c = [3.0, 4.0], [6.0, 8.0]
    show("cosine of parallel vectors", (a[0] * c[0] + a[1] * c[1]) / (5 * 10), 1.0)
    show("dot of same vectors (length leaks in)", a[0] * c[0] + a[1] * c[1], 50.0)


def page04():
    OUT.append("[04] Evaluation and statistics")
    from math import comb, erfc, sqrt
    from statistics import NormalDist
    import random
    n, b, c = 30, 18, 12
    tail = Fraction(sum(comb(n, k) for k in range(b, n + 1)), 2 ** n)
    show("P(X >= 18 | n=30, p=1/2) exact", round(float(tail), 6), 0.180797)
    show("sum C(30,k) k=18..30", sum(comb(n, k) for k in range(b, n + 1)), 194129627)
    show("2^30", 2 ** 30, 1073741824)
    p_two = float(2 * tail)
    show("two-sided exact sign test p", round(p_two, 4), 0.3616)
    chi2 = lambda x: erfc(sqrt(x / 2))       # survival function of chi-square with 1 df
    show("McNemar chi2 no correction (b-c)^2/(b+c)", (b - c) ** 2 / (b + c), 1.2)
    show("  p", round(chi2(1.2), 4), 0.2733)
    show("McNemar chi2 continuity (|b-c|-1)^2/(b+c)", round((abs(b - c) - 1) ** 2 / (b + c), 4), 0.8333)
    show("  p", round(chi2(25 / 30), 4), 0.3613)
    # discordant counts consistent with 156 and 162 out of 200
    both_right = 156 - 12
    show("both right = A right - (A right, B wrong)", both_right, 144)
    show("check B right = both + 18", both_right + 18, 162)
    show("both wrong", 200 - both_right - 18 - 12, 26)
    # wrong: unpaired two-proportion z test
    p1, p2 = 156 / 200, 162 / 200
    pool = (156 + 162) / 400
    se = sqrt(pool * (1 - pool) * (1 / 200 + 1 / 200))
    z = (p2 - p1) / se
    show("pooled p", pool, 0.795)
    show("unpaired SE", round(se, 4), 0.0404)
    show("unpaired z", round(z, 3), 0.743)
    show("unpaired two-sided p", round(2 * (1 - NormalDist().cdf(z)), 3), 0.457)
    # paired z (normal approx to McNemar without correction) equals sqrt(1.2)
    show("paired z = (b-c)/sqrt(b+c)", round((b - c) / sqrt(b + c), 4), 1.0954)
    # how lopsided would 30 discordant need to be? smallest b with two-sided p < 0.05
    def p_exact(bb, nn):
        k = max(bb, nn - bb)
        return min(1.0, 2 * sum(comb(nn, j) for j in range(k, nn + 1)) / 2 ** nn)
    crit = min(bb for bb in range(16, 31) if p_exact(bb, 30) < 0.05)
    show("smallest wins out of 30 for p < 0.05", crit, 21)
    show("  p at 21/30", round(p_exact(21, 30), 4), 0.0428)
    show("  p at 20/30", round(p_exact(20, 30), 4), 0.0987)
    # power of the exact test if B truly wins 60% of discordant pairs
    power = sum(comb(30, k) * 0.6 ** k * 0.4 ** (30 - k) for k in range(21, 31)) + sum(comb(30, k) * 0.6 ** k * 0.4 ** (30 - k) for k in range(0, 10))
    show("power with 30 discordant, true 60/40", round(power, 3), 0.177)
    # discordant pairs needed for 80% power at 60/40 (normal approx)
    za, zb = NormalDist().inv_cdf(0.975), NormalDist().inv_cdf(0.8)
    nd = ((za * 0.5 + zb * sqrt(0.6 * 0.4)) / 0.1) ** 2
    show("z_0.975", round(za, 4), 1.96)
    show("z_0.80", round(zb, 4), 0.8416)
    show("discordant pairs needed", math.ceil(nd), 194)
    show("questions needed at 15% discordance", math.ceil(math.ceil(nd) / 0.15), 1294)
    # unpaired sample size per arm for 78% vs 81%
    pbar = (0.78 + 0.81) / 2
    nu = (za * sqrt(2 * pbar * (1 - pbar)) + zb * sqrt(0.78 * 0.22 + 0.81 * 0.19)) ** 2 / 0.03 ** 2
    show("unpaired n per arm (78% vs 81%, 80% power)", math.ceil(nu), 2842)
    # Wilson intervals
    def wilson(k, nn, zz=1.959964):
        ph = k / nn
        den = 1 + zz * zz / nn
        cen = (ph + zz * zz / (2 * nn)) / den
        half = zz * sqrt(ph * (1 - ph) / nn + zz * zz / (4 * nn * nn)) / den
        return round(cen - half, 4), round(cen + half, 4)
    show("Wilson 95% for 162/200", wilson(162, 200), (0.75, 0.8583))
    show("Wilson 95% for 156/200", wilson(156, 200), (0.7176, 0.8318))
    show("Wald 95% for 162/200", (round(0.81 - 1.96 * sqrt(0.81 * 0.19 / 200), 4), round(0.81 + 1.96 * sqrt(0.81 * 0.19 / 200), 4)), (0.7556, 0.8644))
    show("Wilson for 10/10", wilson(10, 10), (0.7225, 1.0))
    show("Wald for 10/10 (degenerate)", (1.0, 1.0), (1.0, 1.0))
    show("SE of accuracy p=0.8, n=200", round(sqrt(0.8 * 0.2 / 200), 4), 0.0283)
    show("  95% half-width (points)", round(1.96 * sqrt(0.8 * 0.2 / 200) * 100, 1), 5.5)
    # paired bootstrap of the accuracy difference (seeded)
    pairs = [(1, 1)] * 144 + [(0, 1)] * 18 + [(1, 0)] * 12 + [(0, 0)] * 26
    rng = random.Random(0)
    diffs = []
    for _ in range(10000):
        sample = [pairs[rng.randrange(200)] for _ in range(200)]
        diffs.append(sum(bb - aa for aa, bb in sample) / 200)
    diffs.sort()
    lo, hi = diffs[249], diffs[9749]
    show("paired bootstrap 95% CI for B - A (seed 0, 10k)", (round(lo, 3), round(hi, 3)), (-0.025, 0.085))
    show("sign test 40 vs 20 (n=60) two-sided p", round(p_exact(40, 60), 4), 0.0135)
    # multiple comparisons
    show("P(>=1 false positive) over 20 tests at 0.05", round(1 - 0.95 ** 20, 4), 0.6415)
    show("Bonferroni threshold for 20 tests", 0.05 / 20, 0.0025)


def page05():
    OUT.append("[05] Agents")
    caps = [min(30.0, 0.5 * 2 ** a) for a in range(8)]
    show("backoff caps base 0.5, cap 30, attempts 0..7", caps, [0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 30.0, 30.0])
    show("expected full-jitter delay at attempt 3 (cap/2)", caps[3] / 2, 2.0)
    show("worst-case total wait over 5 retries (sum of caps 0..4)", sum(caps[:5]), 15.5)
    show("P(all 3 tries fail) if each fails independently 20%", round(0.2 ** 3, 4), 0.008)


def page06():
    OUT.append("[06] Decoding and sampling")
    def sm(z, T=1.0):
        m = max(z)
        e = [math.exp((x - m) / T) for x in z]
        return [x / sum(e) for x in e]
    r = lambda v: [round(x, 4) for x in v]
    show("softmax [2,1,0] T=1", r(sm([2, 1, 0])), [0.6652, 0.2447, 0.09])
    show("softmax [2,1,0] T=0.5", r(sm([2, 1, 0], 0.5)), [0.8668, 0.1173, 0.0159])
    show("softmax [2,1,0] T=2", r(sm([2, 1, 0], 2)), [0.5065, 0.3072, 0.1863])
    show("e^2, e^1, e^0 sum", round(math.exp(2) + math.exp(1) + 1, 4), 11.1073)
    show("top-k=2 on [2,1,0] renormalized", r([math.exp(2) / (math.exp(2) + math.e), math.e / (math.exp(2) + math.e)]), [0.7311, 0.2689])
    pr = [0.5, 0.3, 0.15, 0.05]
    show("top-p 0.75 keeps 2 -> renormalized", r([0.5 / 0.8, 0.3 / 0.8]), [0.625, 0.375])
    show("top-p 0.9 keeps 3 -> renormalized", r([x / 0.95 for x in pr[:3]]), [0.5263, 0.3158, 0.1579])
    show("min-p 0.2 threshold = 0.2 * 0.5", 0.2 * 0.5, 0.1)
    show("min-p 0.2 keeps", [x for x in pr if x >= 0.1], [0.5, 0.3, 0.15])
    # flat distribution: top-p 0.75 keeps many, min-p 0.2 keeps those >= 0.2*max
    flat = [0.12] * 5 + [0.08] * 5
    show("flat dist sums to 1", round(sum(flat), 10), 1.0)
    acc, kept = 0, 0
    for x in sorted(flat, reverse=True):
        kept += 1
        acc += x
        if acc >= 0.75 - 1e-12:
            break
    show("flat: top-p 0.75 keeps", kept, 7)
    show("rep penalty 1.2 on logit 2.0", round(2.0 / 1.2, 4), 1.6667)
    show("rep penalty 1.2 on logit -1.0", -1.0 * 1.2, -1.2)
    show("freq 0.5 x count 3 + presence 0.6 on logit 2.0", round(2.0 - 0.5 * 3 - 0.6, 4), -0.1)
    lp = [-0.1, -0.5, -2.0]
    show("mean logprob", round(sum(lp) / 3, 4), -0.8667)
    show("perplexity exp(-mean)", round(math.exp(-sum(lp) / 3), 3), 2.379)
    show("prob of sequence exp(sum)", round(math.exp(sum(lp)), 4), 0.0743)
    show("logprob -0.1 -> prob", round(math.exp(-0.1), 4), 0.9048)
    # beam example where width 2 misses the optimum
    st = [-0.5, -1.0, -2.0]
    tr = [[-2.0, -2.0, -2.0], [-0.5, -2.0, -1.0], [-2.0, -4.0, -2.0]]
    sc = lambda q: st[q[0]] + sum(tr[a][b] for a, b in zip(q, q[1:]))
    show("greedy [0,0,0]", sc([0, 0, 0]), -4.5)
    show("beam2 [1,0,0]", sc([1, 0, 0]), -3.5)
    show("optimum [0,1,0]", sc([0, 1, 0]), -3.0)
    show("step-2 beam: [1,0], [1,2]", (sc([1, 0]), sc([1, 2])), (-1.5, -2.0))
    show("pruned prefix [0,1]", sc([0, 1]), -2.5)
    # length normalization
    show("short: -3.0/3", -3.0 / 3, -1.0)
    show("long: -4.0/8", -4.0 / 8, -0.5)
    show("GNMT-style lp(8), alpha 0.6: ((5+8)/6)^0.6", round(((5 + 8) / 6) ** 0.6, 4), 1.5903)


def page10():
    OUT.append("[10] Practice quiz numeric answers")
    from math import comb
    show("Q1 KV per token KiB (32, 8, 128, fp16)", kv(32, 8, 128, 1, 1, 2) / KiB, 128.0)
    show("Q2 70B bf16 GB", 70e9 * 2 / GB, 140.0)
    show("Q4 KV 40 layers, 8 kv, 128, fp8, 16 x 4096 GiB", kv(40, 8, 128, 4096, 16, 1) / GiB, 5.0)
    show("Q6 spec a=0.6 k=4", round((1 - 0.6 ** 5) / 0.4, 2), 2.31)
    show("Q9 13B fp16 on 2 TB/s ms/token", 26e9 / 2e12 * 1e3, 13.0)
    show("Q10 LoRA r=8 on 4096x4096 + 4096x1024", 8 * (4096 + 4096) + 8 * (4096 + 1024), 106496)
    show("Q13 DPO loss at init", round(math.log(2), 3), 0.693)
    show("Q15 idf N=10 n=1", round(math.log(1 + 9.5 / 1.5), 4), 1.9924)
    show("Q16 RRF ranks 1 and 4", round(1 / 61 + 1 / 64, 4), 0.032)
    show("Q17 recall@5 2 of 8", 2 / 8, 0.25)
    show("Q18 precision@4 3 of 4", 3 / 4, 0.75)
    show("Q20 nDCG@2 ranked [1,3] ideal [3,1]", round((1 + 3 / math.log2(3)) / (3 + 1 / math.log2(3)), 4), 0.7967)
    show("Q23 sign test 9 vs 1", round(2 * (comb(10, 9) + comb(10, 10)) / 2 ** 10, 4), 0.0215)
    show("Q25 SE 90% over 400", round(math.sqrt(0.9 * 0.1 / 400), 4), 0.015)
    show("Q27 Bonferroni 5 tests", 0.05 / 5, 0.01)
    show("Q31 full jitter ceiling attempt 4", min(30, 0.5 * 2 ** 4), 8.0)
    show("Q33 softmax [1,0] first", round(math.e / (math.e + 1), 4), 0.7311)
    acc, kept = 0, 0
    for x in [0.4, 0.3, 0.2, 0.1]:
        kept += 1
        acc += x
        if acc >= 0.6 - 1e-12:
            break
    show("Q34 top-p 0.6 keeps", kept, 2)
    show("Q37 min-p 0.1 x 0.6", round(0.1 * 0.6, 4), 0.06)
    show("Q39 smallest intersection with union 10 for 5I >= 4U", min(i for i in range(11) if 5 * i >= 40), 8)
    show("Q41 F1 with P=0.5 R=1", round(2 * 0.5 * 1 / 1.5, 4), 0.6667)
    show("Q43 CE -ln 0.25", round(-math.log(0.25), 4), 1.3863)
    show("Q45 MLP 10-5-1 params with biases", (10 * 5 + 5) + (5 * 1 + 1), 61)
    show("Q47 12 L d^2, L=24, d=2048, billions", round(12 * 24 * 2048 ** 2 / 1e9, 2), 1.21)
    show("Q48 6ND N=1e9 D=20e9 in 1e20 units", round(6 * 1e9 * 20e9 / 1e20, 2), 1.2)
    show("Q51 Chinchilla tokens for 3B, billions", 3 * 20, 60)
    pos, neg = [0.8, 0.6], [0.7, 0.2]
    show("Q54 AUC", sum(1 for a in pos for b in neg if a > b) / 4, 0.75)
    show("Q55 2M req/day avg QPS", round(2e6 / 86400, 2), 23.15)
    show("Q56 Little's law 20 x 5", 20 * 5, 100)
    show("Q58 cascade 0.7*1 + 0.3*8", round(0.7 * 1 + 0.3 * 8, 2), 3.1)


def foundations():
    OUT.append("[F1] ML foundations")
    TP, FP, FN, TN = 40, 10, 20, 930
    P, R = TP / (TP + FP), TP / (TP + FN)
    show("precision", P, 0.8)
    show("recall", round(R, 4), 0.6667)
    show("F1", round(2 * P * R / (P + R), 4), 0.7273)
    show("F2", round(5 * P * R / (4 * P + R), 4), 0.6897)
    show("accuracy", (TP + TN) / 1000, 0.97)
    show("accuracy of always-negative", (FP + TN) / 1000, 0.94)
    show("specificity", round(TN / (TN + FP), 4), 0.9894)
    show("FPR", round(FP / (FP + TN), 4), 0.0106)
    show("CE -ln 0.8", round(-math.log(0.8), 4), 0.2231)
    show("CE -ln 0.5", round(-math.log(0.5), 4), 0.6931)
    show("CE -ln 0.01", round(-math.log(0.01), 4), 4.6052)
    show("BCE y=0, p=0.9", round(-math.log(0.1), 4), 2.3026)
    y, yh = [3, 5, 2], [2.5, 5, 4]
    mse = sum((a - b) ** 2 for a, b in zip(y, yh)) / 3
    show("MSE", round(mse, 4), 1.4167)
    show("MAE", round(sum(abs(a - b) for a, b in zip(y, yh)) / 3, 4), 0.8333)
    show("RMSE", round(math.sqrt(mse), 4), 1.1902)
    w, ws = 0.0, []
    for _ in range(3):
        w -= 0.1 * 2 * (w - 3)
        ws.append(round(w, 4))
    show("GD on (w-3)^2, lr 0.1, 3 steps", ws, [0.6, 1.08, 1.464])
    w, ws = 0.0, []
    for _ in range(3):
        w -= 1.1 * 2 * (w - 3)
        ws.append(round(w, 3))
    show("GD lr 1.1 diverges", ws, [6.6, -1.32, 8.184])
    g = 0.5
    m, v = 0.1 * g, 0.001 * g * g
    show("Adam first step size (lr 1e-3)", round((m / 0.1) / (math.sqrt(v / 0.001) + 1e-8) * 1e-3, 6), 0.001)
    sig = lambda z: 1 / (1 + math.exp(-z))
    show("sigmoid(2)", round(sig(2), 4), 0.8808)
    show("logistic p for w=0.5, x=2", round(sig(1.0), 4), 0.7311)
    show("logistic grad (p - y) x with y=1", round((sig(1.0) - 1) * 2, 4), -0.5379)
    pos, neg = [0.9, 0.8, 0.4], [0.7, 0.3, 0.2, 0.1]
    wins = sum(1 if a > b else 0.5 if a == b else 0 for a in pos for b in neg)
    show("AUC pairs won", wins, 11)
    show("AUC", round(wins / 12, 4), 0.9167)
    show("entropy 80/20 (bits)", round(-(0.8 * math.log2(0.8) + 0.2 * math.log2(0.2)), 4), 0.7219)
    show("gini 80/20", round(1 - 0.64 - 0.04, 4), 0.32)

    OUT.append("[F2] Transformers")
    V, d, L, ff = 32000, 4096, 32, 11008
    show("Llama-2-7B attention params/layer 4d^2", 4 * d * d, 67108864)
    show("Llama-2-7B MLP params/layer 3 d ff", 3 * d * ff, 135266304)
    total = L * (4 * d * d + 3 * d * ff + 2 * d) + 2 * V * d + d
    show("Llama-2-7B total params", total, 6738415616)
    show("12 L d^2 rule of thumb", 12 * L * d * d, 6442450944)
    tot3 = L * (2 * d * d + 2 * d * 1024 + 3 * d * 14336 + 2 * d) + 2 * 128256 * d + d
    show("Llama-3-8B total params", tot3, 8030261248)
    q, K, Vv = [1, 0], [[1, 0], [0, 1], [1, 1]], [[1, 0], [0, 1], [1, 1]]
    sc = [(q[0] * k[0] + q[1] * k[1]) / math.sqrt(2) for k in K]
    e = [math.exp(x - max(sc)) for x in sc]
    a = [x / sum(e) for x in e]
    show("toy attention scores", [round(x, 4) for x in sc], [0.7071, 0.0, 0.7071])
    show("toy attention weights", [round(x, 4) for x in a], [0.4011, 0.1978, 0.4011])
    show("toy attention output", [round(sum(a[i] * Vv[i][j] for i in range(3)), 4) for j in range(2)], [0.8022, 0.5989])
    show("std of unscaled q.k at d=128", round(math.sqrt(128), 2), 11.31)
    show("8192x8192 fp16 score matrix per head MiB", 8192 * 8192 * 2 / MiB, 128.0)
    show("  x 32 heads GiB", 8192 * 8192 * 2 * 32 / GiB, 4.0)
    show("sin(1), cos(1)", (round(math.sin(1), 4), round(math.cos(1), 4)), (0.8415, 0.5403))
    show("Llama-3 embedding table bf16 GB", round(128256 * 4096 * 2 / 1e9, 2), 1.05)
    show("Mixtral active fraction 12.9/46.7", round(12.9 / 46.7, 3), 0.276)

    OUT.append("[F3] Training and scaling")
    F = 6 * 6.74e9 * 2e12
    show("6ND for 6.74B params, 2T tokens", F, 8.088e22, tol=1e18)
    show("A100-hours at 40% MFU (312 TFLOPS)", round(F / (312e12 * 0.4) / 3600), 180021)
    show("Chinchilla tokens for 70B (20/param), T", 70e9 * 20 / 1e12, 1.4)
    show("inference FLOPs/token 2N for 6.74B, GFLOP", 2 * 6.74e9 / 1e9, 13.48)
    show("perplexity from CE 2.0 nats", round(math.exp(2.0), 3), 7.389)
    show("CE from perplexity 10", round(math.log(10), 4), 2.3026)

    from math import comb
    show("pass@1, n=10 samples, c=3 correct", round(1 - comb(7, 1) / comb(10, 1), 4), 0.3)
    show("pass@5, n=10, c=3: 1 - C(7,5)/C(10,5)", round(1 - comb(7, 5) / comb(10, 5), 4), 0.9167)
    show("C(7,5), C(10,5)", (comb(7, 5), comb(10, 5)), (21, 252))
    show("Llama 3 8B tokens/param (15T / 8B)", round(15e12 / 8e9), 1875)
    show("GPT-3 tokens/param (300B / 175B)", round(300 / 175, 2), 1.71)
    show("7B full FT state (16 B/param) across 8 GPUs with ZeRO-3, GB each", 7e9 * 16 / 8 / 1e9, 14.0)
    show("ZeRO-1 (shard optimizer states 12 B/param of 16) per GPU of 8, GB", round(7e9 * (4 + 12 / 8) / 1e9, 1), 38.5)
    show("MLP 3-4-2 params with biases", (3 * 4 + 4) + (4 * 2 + 2), 26)
    show("one MHA layer 12 d^2 at d=4096", 12 * 4096 ** 2, 201326592)
    show("Llama-2-7B layer total", 4 * 4096 ** 2 + 3 * 4096 * 11008 + 2 * 4096, 202383360)
    show("MLP share of layer", round(3 * 4096 * 11008 / 202383360, 3), 0.668)

    maj = sum(comb(5, k) * 0.6 ** k * 0.4 ** (5 - k) for k in range(3, 6))
    show("majority of 5 independent samples, each right w.p. 0.6", round(maj, 4), 0.6826)
    maj9 = sum(comb(9, k) * 0.6 ** k * 0.4 ** (9 - k) for k in range(5, 10))
    show("majority of 9", round(maj9, 4), 0.7334)

    OUT.append("[12] System design estimates")
    qps = 1e6 / 86400
    show("1M requests/day average QPS", round(qps, 2), 11.57)
    show("peak QPS at 3x", round(3 * qps), 35)
    show("peak output tokens/s (300 each)", 35 * 300, 10500)
    show("input tokens/day (1500 each), B", 1e6 * 1500 / 1e9, 1.5)
    show("output tokens/day (300 each), M", 1e6 * 300 / 1e6, 300.0)
    show("cost/day at $0.50/M in, $1.50/M out (illustrative)", 1500 * 0.5 + 300 * 1.5, 1200.0)
    show("Little's law: 35 req/s x 10 s in system", 35 * 10, 350)
    show("KV per sequence 1800 tokens (Llama-3-8B fp16) MB", round(1800 * 131072 / 1e6, 1), 235.9)
    show("KV for 350 concurrent sequences GB", round(350 * 1800 * 131072 / 1e9, 1), 82.6)
    show("GPUs needed at 2500 tok/s each (illustrative), ceil", math.ceil(10500 / 2500), 5)

    show("cascade: 80% small (cost 1) + 20% large (cost 10), avg cost", 0.8 * 1 + 0.2 * 10, 2.8)
    show("  savings vs all-large", round(1 - 2.8 / 10, 2), 0.72)
    show("cascade with router on every request (cost 0.1)", round(0.1 + 2.8, 1), 2.9)
    show("semantic cache 30% hit rate: calls/day of 1M", round(1e6 * 0.7), 700000)
    show("latency: TTFT 0.5 s + 300 tokens x 20 ms", 0.5 + 300 * 0.02, 6.5)
    show("p95 budget: retrieval 150 + rerank 100 + TTFT 600 ms", 150 + 100 + 600, 850)

    show("10M vectors x 1024 dims x 4 B, GB", 10e6 * 1024 * 4 / GB, 40.96)
    show("100k questions/day avg QPS", round(1e5 / 86400, 2), 1.16)

    OUT.append("[04+] Classic text metrics")
    from collections import Counter
    ref, cand = Counter("the cat sat on the mat".split()), Counter("the cat is on the mat".split())
    show("ROUGE-1 overlap (clipped) for 'the cat sat on the mat' vs 'the cat is on the mat'", sum((ref & cand).values()), 5)
    show("ROUGE-1 recall = precision", round(5 / 6, 4), 0.8333)
    show("token F1: pred 'Paris France', gold 'Paris'", round(2 * 0.5 * 1.0 / 1.5, 4), 0.6667)


if __name__ == "__main__":
    foundations()
    page01()
    page02()
    page03()
    page04()
    page05()
    page06()
    page10()
    print("\n".join(OUT))
    print(f"verify_numbers: all {sum(1 for l in OUT if ' = ' in l)} values verified")
