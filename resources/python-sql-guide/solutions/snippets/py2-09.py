from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    PAID = auto()
    SHIPPED = auto()

s = Status.PAID
print(s, s.name, s.value, Status["SHIPPED"], [m.name for m in Status])
print(s is Status.PAID, s == Status.PENDING)
