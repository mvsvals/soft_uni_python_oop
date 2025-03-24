class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False

from unittest import TestCase, main

class TestCat(TestCase):
    def setUp(self):
        self.example_cat = Cat('Example')

    def test_cat_init(self):
        self.assertEqual('Example', self.example_cat.name)
        self.assertFalse(self.example_cat.fed)
        self.assertFalse(self.example_cat.sleepy)
        self.assertEqual(0, self.example_cat.size)

    def test_cat_eat_if_hungry(self):
        self.example_cat.eat()
        self.assertTrue(self.example_cat.fed)
        self.assertTrue(self.example_cat.sleepy)
        self.assertEqual(1, self.example_cat.size)

    def test_cat_eat_if_already_fed(self):
        self.example_cat.eat()
        with self.assertRaises(Exception) as e:
            self.example_cat.eat()
        self.assertEqual('Already fed.', str(e.exception))

    def test_cat_sleep_not_hungry(self):
        self.example_cat.eat()
        self.example_cat.sleep()
        self.assertFalse(self.example_cat.sleepy)

    def test_cat_sleep_while_hungry(self):
        with self.assertRaises(Exception) as e:
            self.example_cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(e.exception))

if __name__ == '__main__':
    main()



