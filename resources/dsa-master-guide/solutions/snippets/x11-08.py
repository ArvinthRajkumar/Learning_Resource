class Node:
    def __init__(self): self.children, self.content = {}, None
class FileSystem:
    def __init__(self): self.root = Node()
    def _walk(self, path, create=False):
        node = self.root
        for part in [p for p in path.split("/") if p]:
            if part not in node.children:
                if not create: raise FileNotFoundError(path)
                node.children[part] = Node()
            node = node.children[part]
        return node
    def mkdir(self, path): self._walk(path, create=True)
    def add_file(self, path, content):
        node = self._walk(path, create=True); node.content = (node.content or "") + content
    def ls(self, path):
        node = self._walk(path)
        if node.content is not None: return [path.rstrip("/").split("/")[-1]]
        return sorted(node.children)
    def read(self, path):
        node = self._walk(path)
        if node.content is None: raise IsADirectoryError(path)
        return node.content
fs = FileSystem()
fs.mkdir("/a/b/c"); fs.add_file("/a/b/c/d.txt", "hello"); fs.add_file("/a/b/c/d.txt", " world"); fs.add_file("/a/z.txt", "z")
assert fs.ls("/") == ["a"] and fs.ls("/a") == ["b", "z.txt"] and fs.ls("/a/b/c/d.txt") == ["d.txt"] and fs.read("/a/b/c/d.txt") == "hello world"
try: fs.read("/a/b")
except IsADirectoryError: pass
try: fs.ls("/nope")
except FileNotFoundError: pass
print("file system tests passed; listing /a:", fs.ls("/a"))
