import random
def fake_generate(seed, prompt):                               # a stand-in: the "image" is determined by seed and prompt
    r = random.Random(f"{seed}|{prompt}"); return [round(r.random(), 2) for _ in range(5)]
print("same seed and prompt  :", fake_generate(7, "a cat") == fake_generate(7, "a cat"))
print("different seed        :", fake_generate(7, "a cat") != fake_generate(8, "a cat"))
print("same seed, new prompt :", fake_generate(7, "a cat") != fake_generate(7, "a dog"))
