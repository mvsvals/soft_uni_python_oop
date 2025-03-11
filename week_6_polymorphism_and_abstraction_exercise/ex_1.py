from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
    @abstractmethod
    def drive(self, distance):
        pass
    @abstractmethod
    def refuel(self, amount):
        pass


class Car(Vehicle):
    INCREASED_FUEL_CONSUMPTION = 0.9
    def drive(self, distance):
        actual_fuel_consumption = Car.INCREASED_FUEL_CONSUMPTION + self.fuel_consumption
        fuel_needed = distance * actual_fuel_consumption
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, amount):
        self.fuel_quantity += amount

class Truck(Vehicle):
    INCREASED_FUEL_CONSUMPTION = 1.6

    def drive(self, distance):
        actual_fuel_consumption = Truck.INCREASED_FUEL_CONSUMPTION + self.fuel_consumption
        fuel_needed = distance * actual_fuel_consumption
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, amount):
        self.fuel_quantity += 0.95 * amount