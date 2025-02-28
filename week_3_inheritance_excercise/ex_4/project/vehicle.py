class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.horse_power = horse_power
        self.fuel = fuel

    def drive(self, kilometres):
        fuel_needed = self.fuel_consumption * kilometres
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed

