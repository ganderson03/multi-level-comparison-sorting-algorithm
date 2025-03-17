import unittest
from src.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_sorted_list(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(bubble_sort([3, 1, 4, 2, 5]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(bubble_sort([42]), [42])

    def test_duplicate_elements(self):
        self.assertEqual(bubble_sort([3, 1, 2, 3, 2]), [1, 2, 2, 3, 3])

if __name__ == '__main__':
    unittest.main()