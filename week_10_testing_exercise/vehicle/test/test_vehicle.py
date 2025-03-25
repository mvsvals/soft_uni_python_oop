from unittest import TestCase, main
from project.vehicle import Vehicle

class TestVehicle(TestCase):
    
    def setUp(self):
        self.dummy_vehicle = Vehicle(20, 240)

    def test_vehicle_init(self):
        self.assertEqual(20, self.dummy_vehicle.fuel)
        self.assertEqual(240, self.dummy_vehicle.horse_power)
        self.assertEqual(20, self.dummy_vehicle.capacity)
        self.assertEqual(1.25, self.dummy_vehicle.fuel_consumption)

    def test_drive_with_insufficient_fuel_raises(self):
        self.assertEqual(20, self.dummy_vehicle.fuel)
        with self.assertRaises(Exception) as e:
            self.dummy_vehicle.drive(3000)
        self.assertEqual("Not enough fuel", str(e.exception))
        self.assertEqual(20, self.dummy_vehicle.fuel)

    def test_drive_with_sufficient_fuel(self):
        self.assertEqual(20, self.dummy_vehicle.fuel)
        self.dummy_vehicle.drive(3)
        self.assertEqual(16.25, self.dummy_vehicle.fuel)

    def test_refuel_with_overloaded_capacity_raises(self):
        self.assertEqual(20, self.dummy_vehicle.fuel)
        with self.assertRaises(Exception) as e:
            self.dummy_vehicle.refuel(1500)
        self.assertEqual("Too much fuel", str(e.exception))
        self.assertEqual(20, self.dummy_vehicle.fuel)

    def test_refuel_with_normal_capacity(self):
        self.dummy_vehicle.drive(4)
        self.assertEqual(15, self.dummy_vehicle.fuel)
        self.dummy_vehicle.refuel(5)
        self.assertEqual(20, self.dummy_vehicle.fuel)


    def test_str(self):
        result = str(self.dummy_vehicle)
        self.assertEqual(f"The vehicle has 240 horse power with 20 fuel left and 1.25 fuel consumption", result)


if __name__ == '__main__':
    main()