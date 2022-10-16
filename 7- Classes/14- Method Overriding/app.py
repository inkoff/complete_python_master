class Animal:
    def __init__(self):
        print("Animal constr")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal constr")
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
# print(m.weight)  # AttributeError: 'Mammal' object has no attribute 'age'
print(m.weight)
