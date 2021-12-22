import unittest
from merge_sort import merge_sort
from utils import generate_random_array

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.test_array = generate_random_array(40)

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.test_array), sorted(self.test_array))



if __name__ == "__main__":
    unittest.main()