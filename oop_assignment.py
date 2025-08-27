# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Vehicle is moving...")

    def info(self):
        print(f"{self.brand} {self.model}")


# Subclass 1
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def move(self):
        print(f"{self.brand} {self.model} is Driving 🚗")


# Subclass 2
class Plane(Vehicle):
    def __init__(self, brand, model, engines):
        super().__init__(brand, model)
        self.engines = engines

    def move(self):
        print(f"{self.brand} {self.model} is Flying ✈️")


# Subclass 3
class Boat(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def move(self):
        print(f"{self.brand} {self.model} is Sailing 🚤")


# Testing Polymorphism
vehicles = [
    Car("Toyota", "Corolla", 4),
    Plane("Boeing", "747", 4),
    Boat("Yamaha", "WaveRunner", 3)
]

for v in vehicles:
    v.info()
    v.move()
    print()
