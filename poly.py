class Animal:
    def make_sound(self):
        print("Some generic  sounds.")
class Dog(Animal):
    def make_sound(self):
        print("Barking")
class Cat(Animal):
    def make_sound(self):
        print("Meowing")
animals=[Dog(),Cat()]

