import unittest
from src.timsort import timsort

class TestTimsort(unittest.TestCase):
    
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(timsort(arr), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(timsort(arr), [1, 2, 3, 4, 5])
    
    def test_random_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        self.assertEqual(timsort(arr), sorted(arr))
    
    def test_empty_array(self):
        arr = []
        self.assertEqual(timsort(arr), [])
    
    def test_single_element_array(self):
        arr = [42]
        self.assertEqual(timsort(arr), [42])

if __name__ == '__main__':
    unittest.main()