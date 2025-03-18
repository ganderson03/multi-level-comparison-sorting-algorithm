
# Sorting Algorithms Project

This project implements three sorting algorithms in Python: Bubble Sort, Quicksort, and Timsort. Each algorithm is implemented in its own module within the `src` directory, and unit tests are provided in the `tests` directory to ensure the correctness of each implementation.

## Algorithms

1. **Bubble Sort**: A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

2. **Quicksort**: An efficient sorting algorithm that uses a divide-and-conquer approach to sort elements. It selects a 'pivot' element and partitions the other elements into two sub-arrays according to whether they are less than or greater than the pivot.

3. **Timsort**: A hybrid sorting algorithm derived from merge sort and insertion sort. It is designed to perform well on many kinds of real-world data and is the default sorting algorithm in Python's built-in `sorted()` function.

## Project Structure

```
sorting-algorithms
├── src
│   ├── __init__.py
│   ├── bubble_sort.py
│   ├── quicksort.py
│   ├── timsort.py
│   └── utils
│       └── __init__.py
├── tests
│   ├── __init__.py
│   ├── test_bubble_sort.py
│   ├── test_quicksort.py
│   └── test_timsort.py
├── requirements.txt
└── README.md
```

## Running Tests

To run the tests for the sorting algorithms, you can use a testing framework such as `pytest`. Make sure to install the required dependencies listed in `requirements.txt` and then execute the tests with the following command:

```bash
pytest tests/
```

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

You can import the sorting algorithms in your Python code as follows:

```python
from src.bubble_sort import bubble_sort
from src.quicksort import quicksort
from src.timsort import timsort
```

Feel free to explore the implementations and tests to understand how each algorithm works!