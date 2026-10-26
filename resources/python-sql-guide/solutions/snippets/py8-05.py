class A:
    kind = "class attribute"
    def who(self): return "A.who"
class B(A):
    def who(self): return "B.who -> " + super().who()
class C(A):
    def who(self): return "C.who -> " + super().who()
class D(B, C): pass
print([k.__name__ for k in D.__mro__])
print(D().who())
d = D()
print("instance dict empty:", d.__dict__, "| lookup finds class attribute:", d.kind)
d.kind = "instance attribute"
print("now shadowed on the instance:", d.kind, "| class unchanged:", D.kind)
m = d.who
print("bound method has __self__:", m.__self__ is d, "| underlying function:", m.__func__.__qualname__)
