import unittest
from dynamic_array import DynamicArray
from utils import generate_random_array



class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        self.numbers = generate_random_array(49)

    def test_initialize_dynamic_array(self):
        dynamic_array = DynamicArray()
        for number in self.numbers:
            dynamic_array.append(number)
        self.assertEqual(self.numbers, dynamic_array)
    
    def test_append_dynamic_array(self):
        dynamic_array = DynamicArray([1,2,3,4])
        dynamic_array.append(5)
        self.assertEqual([1,2,3,4,5], dynamic_array)

    def test_insert_dynamic_array(self):
        dynamic_array= DynamicArray([1,2,3,4,5])
        dynamic_array.insert(0,0)
        self.assertEqual([0,1,2,3,4,5], dynamic_array)

    def test_remove_dynamic_array(self):
        dynamic_array= DynamicArray([1,2,3,4,5])
        dynamic_array.remove(0)
        self.assertEqual([2,3,4,5],dynamic_array)

    def test_contains(self):
        dynamic_array= DynamicArray([1,2,3,4,5])
        self.assertTrue(dynamic_array.contains(1))
        self.assertFalse(dynamic_array.contains(6))
    
    def test_index(self):
        dynamic_array= DynamicArray([1,2,3,4,5])
        self.assertEqual(dynamic_array[0],1)
        self.assertRaises(IndexError, lambda : dynamic_array[5])

            
if __name__ == "__main__":
    unittest.main()