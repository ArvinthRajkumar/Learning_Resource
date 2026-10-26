import sys, importlib, types
mod = types.ModuleType("demo_mod")
exec("VALUE = 42\ndef hello(): return 'hi from demo_mod'", mod.__dict__)
sys.modules["demo_mod"] = mod                     # register it like a normal import would
import demo_mod
print(demo_mod.VALUE, demo_mod.hello(), "| cached:", "demo_mod" in sys.modules, "| same object on re-import:", importlib.import_module("demo_mod") is demo_mod)
print("__name__ of the main script:", __name__, "| so `if __name__ == '__main__'` runs only when executed directly")
