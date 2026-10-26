class Temp:
    unit = "C"
    def __init__(self, deg): self.deg = deg
    def to_f(self):                       # needs the instance
        return self.deg * 9 / 5 + 32
    @classmethod
    def from_f(cls, f):                   # alternative constructor; gets the class
        return cls((f - 32) * 5 / 9)
    @staticmethod
    def is_valid(deg):                    # no self or cls; just grouped here
        return deg >= -273.15

t = Temp.from_f(212)
print(t.deg, t.to_f(), Temp.is_valid(-300))
