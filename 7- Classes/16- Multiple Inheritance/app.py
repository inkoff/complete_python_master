class Employ:
    def greet(self):
        print("Employ")


class Person():
    def greet(self):
        print("Person")


class Meneger(Employ, Person):
    pass


m = Meneger()
m.greet()


class Flyer:
    def fly(self):
        print("fly")


class Swimmer():
    def swim(self):
        print("swim")


class FlyFish(Flyer, Swimmer):
    pass
