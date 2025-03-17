import unittest
from src.quicksort import quicksort

class TestQuicksort(unittest.TestCase):
    
    def test_sorted_array(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(quicksort([3, 1, 4, 2, 5]), [1, 2, 3, 4, 5])

    def test_empty_array(self):
        self.assertEqual(quicksort([]), [])

    def test_single_element_array(self):
        self.assertEqual(quicksort([42]), [42])

    def test_array_with_duplicates(self):
        self.assertEqual(quicksort([3, 1, 2, 3, 2, 1]), [1, 1, 2, 2, 3, 3])

if __name__ == '__main__':
    unittest.main()