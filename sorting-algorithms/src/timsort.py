def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(arr, left, mid, right):
    left_copy = arr[left:mid + 1]
    right_copy = arr[mid + 1:right + 1]

    left_index, right_index = 0, 0
    sorted_index = left

    while left_index < len(left_copy) and right_index < len(right_copy):
        if left_copy[left_index] <= right_copy[right_index]:
            arr[sorted_index] = left_copy[left_index]
            left_index += 1
        else:
            arr[sorted_index] = right_copy[right_index]
            right_index += 1
        sorted_index += 1

    while left_index < len(left_copy):
        arr[sorted_index] = left_copy[left_index]
        left_index += 1
        sorted_index += 1

    while right_index < len(right_copy):
        arr[sorted_index] = right_copy[right_index]
        right_index += 1
        sorted_index += 1

def timsort(arr):
    min_run = 32
    n = len(arr)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size *= 2