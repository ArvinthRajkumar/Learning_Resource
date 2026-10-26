import random
random.seed(1)
# a synthetic pool of 10,000 images with a quality score and a CLIP-style text alignment score
pool = [{"quality": random.gauss(5.2, 1.2), "clip": random.gauss(0.27, 0.05), "group": random.choice(["photo", "art", "diagram"])} for _ in range(10000)]
# the "art" group is systematically scored lower by the quality model (a bias to detect)
for item in pool:
    if item["group"] == "art": item["quality"] -= 0.6
def keep(item, q=5.0, c=0.25): return item["quality"] >= q and item["clip"] >= c
kept = [i for i in pool if keep(i)]
print(f"kept {len(kept):,} of {len(pool):,} images ({len(kept) / len(pool):.0%}) with quality >= 5.0 and CLIP >= 0.25")
for g in ("photo", "art", "diagram"):
    before = sum(i["group"] == g for i in pool) / len(pool); after = sum(i["group"] == g for i in kept) / len(kept)
    print(f"  {g:>8}: {before:.0%} of the pool -> {after:.0%} of the filtered set")
