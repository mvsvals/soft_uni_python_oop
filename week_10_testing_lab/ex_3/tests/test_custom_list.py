from unittest import TestCase, main

from ..custom_list import IntegerList

class TestIntegerList(TestCase):
    def setUp(self):
        self.example_list = IntegerList(1, 2 , 3, 4, 5)
    def test_integer_list_init(self):
        self.assertListEqual([1, 2, 3, 4, 5], self.example_list._IntegerList__data)
    def test_integer_list_init_integers_are_skipped(self):
        new_list = IntegerList('asd', 8.4, [1, 2, 3], 5)
        self.assertListEqual([5], new_list._IntegerList__data)

    def test_get_data(self):
        result = self.example_list.get_data()
        self.assertListEqual([1, 2, 3, 4, 5], result)
        self.assertIs(self.example_list._IntegerList__data, result)

    def test_add_element_not_integer(self):
        with self.assertRaises(ValueError) as e:
            self.example_list.add('asd')
            self.example_list.add(3.5)
            self.example_list.add(True)
        self.assertEqual("Element is not Integer", str(e.exception))
        self.assertListEqual([1, 2, 3, 4, 5], self.example_list._IntegerList__data)

    def test_add_element(self):
        self.assertListEqual([1, 2, 3, 4, 5], self.example_list._IntegerList__data)
        result = self.example_list.add(6)
        self.assertIn(6, self.example_list._IntegerList__data)
        self.assertIs(self.example_list._IntegerList__data, result)

    def test_remove_invalid_index(self):
        length_index = len(self.example_list._IntegerList__data)
        with self.assertRaises(IndexError) as e:
            self.example_list.remove_index(length_index)
            length_index += 1
            self.example_list.remove_index(length_index)
        self.assertEqual("Index is out of range", str(e.exception))

    def test_remove_valid_index(self):
        self.assertListEqual([1, 2, 3, 4, 5], self.example_list._IntegerList__data)
        result = self.example_list.remove_index(1)
        self.assertEqual(2, result)

        self.assertListEqual([1, 3, 4, 5], self.example_list._IntegerList__data)

    def test_get_invalid_index_raises(self):
        length_index = len(self.example_list._IntegerList__data)
        with self.assertRaises(IndexError) as e:
            self.example_list.get(length_index)
            length_index += 1
            self.example_list.get(length_index)
        self.assertEqual("Index is out of range", str(e.exception))

    def test_get_valid_index(self):
        self.assertListEqual([1, 2, 3, 4, 5], self.example_list._IntegerList__data)
        result = self.example_list.get(1)
        self.assertEqual(2, result)
        self.assertListEqual([1, 2, 3, 4, 5], self.example_list._IntegerList__data)

    def test_insert_invalid_index_raises(self):
        length_index = len(self.example_list._IntegerList__data)
        with self.assertRaises(IndexError) as e:
            self.example_list.insert(length_index, 5)
            length_index += 1
            self.example_list.insert(length_index, 5)
        self.assertEqual("Index is out of range", str(e.exception))

    def test_insert_invalid_element_raises(self):
        element = 'asd'
        with self.assertRaises(ValueError) as e:
            self.example_list.insert(0, element)
            element = 3.5
            self.example_list.insert(0, element)
            element = []
            self.example_list.insert(0, element)
        self.assertEqual("Element is not Integer", str(e.exception))

    def test_insert_valid_operation(self):
        self.assertListEqual([1, 2, 3, 4, 5], self.example_list._IntegerList__data)
        result = self.example_list.insert(0, 9)
        self.assertIsNone(result)
        self.assertListEqual([9, 1, 2, 3, 4, 5], self.example_list._IntegerList__data)

    def test_get_biggest(self):
        new_list = IntegerList(3, -2, 100, 8)
        result = new_list.get_biggest()
        self.assertEqual(100, result)

    def test_get_index(self):
        self.assertIn(1, self.example_list._IntegerList__data)
        self.assertEqual(1, self.example_list._IntegerList__data[0])
        result = self.example_list.get_index(1)
        self.assertEqual(0, result)

if __name__ == '__main__':
    main()