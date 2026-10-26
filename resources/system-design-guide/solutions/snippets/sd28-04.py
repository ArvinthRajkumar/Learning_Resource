class RaftNode:
    def __init__(self, nid): self.id, self.term, self.voted_for, self.log, self.commit, self.role, self.alive = nid, 0, None, [], 0, "follower", True
    def last(self): return (self.log[-1][0], len(self.log)) if self.log else (0, 0)    # (term of last entry, length)
class Cluster:
    def __init__(self, n=3): self.nodes = [RaftNode(i) for i in range(n)]
    def alive(self): return [n for n in self.nodes if n.alive]
    def election(self, cand_id):
        c = self.nodes[cand_id]; c.term += 1; c.role = "candidate"; c.voted_for = c.id; votes = 1
        for n in self.alive():
            if n is c: continue
            if n.term < c.term: n.term, n.voted_for = c.term, None        # newer term: reset the vote
            if n.voted_for in (None, c.id) and c.last() >= n.last():       # candidate log at least as up to date
                n.voted_for = c.id; votes += 1
        if votes > len(self.nodes) // 2:
            c.role = "leader"
            for n in self.alive():
                if n is not c: n.role = "follower"
            return True
        c.role = "follower"; return False
    def leader(self): return next((n for n in self.alive() if n.role == "leader"), None)
    def write(self, cmd):
        L = self.leader()
        if L is None: return "no leader"
        L.log.append((L.term, cmd)); acks = 1
        for n in self.alive():
            if n is not L:
                n.log = list(L.log); n.term = L.term; acks += 1               # followers copy the leader's log
        if acks > len(self.nodes) // 2:
            for n in self.alive(): n.commit = len(L.log)
            return "committed"
        return "not committed (no majority)"
cl = Cluster(3)
print("node 0 election won:", cl.election(0))
print("write x=1:", cl.write("x=1"), "| write y=2:", cl.write("y=2"))
cl.nodes[0].alive = False
print("leader crashed; leader now:", cl.leader())
print("node 1 election (term", cl.nodes[1].term + 1, ") won:", cl.election(1))
print("write z=3 with 2 of 3 alive:", cl.write("z=3"))
cl.nodes[2].alive = False
print("write w=4 with 1 of 3 alive:", cl.write("w=4"))
print("logs:", {n.id: [c for _, c in n.log] for n in cl.nodes})
