from unittest import TestCase, main
from project.mammal import Mammal



class TestMammal(TestCase):

    def setUp(self):
        self.dummy_mammal = Mammal('Test', 'Type', 'Moo')

    def test_mammal_init(self):
        self.assertEqual('Test', self.dummy_mammal.name)
        self.assertEqual('Type', self.dummy_mammal.type)
        self.assertEqual('Moo', self.dummy_mammal.sound)
        self.assertEqual('animals', self.dummy_mammal._Mammal__kingdom)

    def test_mammal_make_sound(self):
        result = self.dummy_mammal.make_sound()
        self.assertEqual(f"Test makes Moo", result)

    def test_get_kingdom(self):
        result = self.dummy_mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_info(self):
        result = self.dummy_mammal.info()
        self.assertEqual('Test is of type Type', result)

if __name__ == '__main__':
    main()