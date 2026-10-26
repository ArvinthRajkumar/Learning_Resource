from dataclasses import dataclass
@dataclass
class User:
    id: int
    name: str
class InMemoryUserRepo:
    def __init__(self): self.data = {}
    def add(self, u): self.data[u.id] = u
    def get(self, uid): return self.data.get(uid)
class UserService:
    def __init__(self, repo): self.repo = repo
    def rename(self, uid, name):
        u = self.repo.get(uid)
        if u is None: raise KeyError(f"user {uid} not found")
        u.name = name; self.repo.add(u); return u
repo = InMemoryUserRepo(); repo.add(User(1, "ana"))
print(UserService(repo).rename(1, "Ana B."))
