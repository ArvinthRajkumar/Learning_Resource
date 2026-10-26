class LegacyTemperatureSensor:
    def read_fahrenheit(self): return 98.6
class CelsiusSensor:                                   # the interface the rest of the code wants
    def __init__(self, legacy): self.legacy = legacy
    def read_celsius(self): return round((self.legacy.read_fahrenheit() - 32) * 5 / 9, 1)
print(CelsiusSensor(LegacyTemperatureSensor()).read_celsius())
