import random
random.seed(5)
nodes = [f"n{i}" for i in range(9)]
racks = {n: f"rack{i // 3}" for i, n in enumerate(nodes)}                  # 3 racks of 3 nodes
def place(replicas=3):
    first = random.choice(nodes)
    second = random.choice([n for n in nodes if racks[n] != racks[first]])
    third = random.choice([n for n in nodes if racks[n] == racks[second] and n != second])
    return [first, second, third]
blocks = {f"blk{i}": place() for i in range(6)}
print({b: [f"{n}/{racks[n]}" for n in ns] for b, ns in list(blocks.items())[:2]})
dead = "n4"
under = [b for b, ns in blocks.items() if dead in ns]
for b in under:                                                           # re-replicate to restore 3 copies
    live = [n for n in blocks[b] if n != dead]
    new = random.choice([n for n in nodes if n not in blocks[b]])
    blocks[b] = live + [new]
print(f"node {dead} died: re-replicated {len(under)} block(s); every block still has 3 copies on >= 2 racks:",
      all(len(set(ns)) == 3 and len({racks[n] for n in ns}) >= 2 for ns in blocks.values()))
