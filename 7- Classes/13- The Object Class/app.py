class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):

    def walk(self):
        print("walk")


class Fish(Animal):

    def swim(self):
        print("swim")


mammal = Mammal()

mammal.eat()
print(mammal.age)
print(isinstance(mammal, Mammal))
print(isinstance(mammal, Animal))
print(isinstance(mammal, object))

o = object()

print(issubclass(Mammal, Animal))
