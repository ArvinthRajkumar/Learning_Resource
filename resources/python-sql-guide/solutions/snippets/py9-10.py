class TextEditor:
    def __init__(self): self.text, self.history = "", []
    def do(self, command):
        command.apply(self); self.history.append(command)
    def undo(self):
        if self.history: self.history.pop().revert(self)
class Insert:
    def __init__(self, s): self.s = s
    def apply(self, ed): ed.text += self.s
    def revert(self, ed): ed.text = ed.text[: -len(self.s)]
ed = TextEditor()
ed.do(Insert("Hello")); ed.do(Insert(", world"))
print(repr(ed.text)); ed.undo(); print(repr(ed.text))
