class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")
class Cat(Animal):
    def fight(self):
        print(f"{self.name} is fighting.")
d=Dog("Bittu")
c=Cat("Chitti")
d.eat()
d.bark()
c.eat()
c.fight()

