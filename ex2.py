class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.make} model {self.model} was started in year {self.year}")

    def stop(self):
        print(f"The {self.make} model {self.model} was stopped in year {self.year}")

car1 = Car("San", "Can", 2022)
car1.start()
car1.stop()
