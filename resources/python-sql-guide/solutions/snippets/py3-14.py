class Plugin:
    registry = {}
    def __init_subclass__(cls, **kw):
        super().__init_subclass__(**kw)
        Plugin.registry[cls.__name__.lower()] = cls

class Csv(Plugin): pass
class Json(Plugin): pass
print(sorted(Plugin.registry))

Dynamic = type("Dynamic", (), {"hello": lambda self: "hi"})   # create a class at runtime
print(Dynamic().hello())
