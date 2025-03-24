from ..car_manager import Car
from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.test_car = Car('BMW', 'X5', 10, 300)

    def test_car_valid_parameters(self):
        self.assertEqual('BMW', self.test_car.make)
        self.assertEqual('X5', self.test_car.model)
        self.assertEqual(10, self.test_car.fuel_consumption)
        self.assertEqual(300, self.test_car.fuel_capacity)
        self.assertEqual(0, self.test_car.fuel_amount)

    def test_make_setter_empty_value_raises(self):
        with self.assertRaises(Exception) as e:
            self.test_car.make = ''
            self.test_car.make = None
            self.test_car.make = []
        self.assertEqual("Make cannot be null or empty!", str(e.exception))

    def test_model_setter_empty_value_raises(self):
        with self.assertRaises(Exception) as e:
            self.test_car.model = ''
            self.test_car.model = None
            self.test_car.model = []
        self.assertEqual("Model cannot be null or empty!", str(e.exception))

    def test_fuel_consumption_setter_zero_or_negative_value_raises(self):
        with self.assertRaises(Exception) as e:
            self.test_car.fuel_consumption = 0
            self.test_car.fuel_consumption = -2
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(e.exception))

    def test_fuel_amount_setter_negative_value_raises(self):
        with self.assertRaises(Exception) as e:
            self.test_car.fuel_amount = -2
        self.assertEqual("Fuel amount cannot be negative!", str(e.exception))

    def test_fuel_capacity_setter_zero_or_negative_value_raises(self):
        with self.assertRaises(Exception) as e:
            self.test_car.fuel_capacity = 0
            self.test_car.fuel_capacity = -2
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(e.exception))

    def test_refuel_zero_or_negative_value_raises(self):
        with self.assertRaises(Exception) as e:
            self.test_car.refuel(0)
            self.test_car.refuel(-2)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(e.exception))


    def test_refuel(self):
        self.assertEqual(0, self.test_car.fuel_amount)
        self.test_car.refuel(10)
        self.assertEqual(10, self.test_car.fuel_amount)

    def test_refuel_over_capacity(self):
        self.assertEqual(0, self.test_car.fuel_amount)
        self.assertEqual(300, self.test_car.fuel_capacity)
        self.test_car.refuel(1000)
        self.assertEqual(300, self.test_car.fuel_amount)

    def test_drive_without_enough_fuel(self):
        self.assertEqual(0, self.test_car.fuel_amount)
        with self.assertRaises(Exception) as e:
            self.test_car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(e.exception))
        self.assertEqual(0, self.test_car.fuel_amount)

    def test_drive(self):
        self.test_car.fuel_amount = 300
        self.test_car.drive(200)
        self.assertEqual(280, self.test_car.fuel_amount)

if __name__ == '__main__':
    main()