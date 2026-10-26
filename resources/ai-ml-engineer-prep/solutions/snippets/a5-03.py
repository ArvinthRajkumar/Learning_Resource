import math
# Online softmax: process scores in chunks while keeping a running max and normaliser.
scores = [2.0, 1.0, 0.1, 3.0, -1.0, 0.5]
values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
m, l, acc = float("-inf"), 0.0, 0.0
for s, v in zip(scores, values):             # one "block" of size 1 for clarity
    m_new = max(m, s)
    scale = math.exp(m - m_new) if m != float("-inf") else 0.0
    l = l * scale + math.exp(s - m_new)
    acc = acc * scale + math.exp(s - m_new) * v
    m = m_new
exp = [math.exp(s - max(scores)) for s in scores]
direct = sum(e * v for e, v in zip(exp, values)) / sum(exp)
print("online %.6f direct %.6f" % (acc / l, direct))
