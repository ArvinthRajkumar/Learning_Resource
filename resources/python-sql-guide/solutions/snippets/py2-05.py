class Animal:
    def __init__(self, name): self.name = name
    def speak(self): return "..."
    def intro(self): return f"{self.name} says {self.speak()}"

class Dog(Animal):
    def speak(self): return "Woof"

class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)            # call the parent initialiser
        self.age = age
    def speak(self): return super().speak() + "!"

for pet in (Animal("Generic"), Dog("Rex"), Puppy("Bit", 1)):
    print(pet.intro())
print(isinstance(Puppy("a", 1), Animal), issubclass(Puppy, Dog))
