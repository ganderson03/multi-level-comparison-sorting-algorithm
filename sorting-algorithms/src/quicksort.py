# Coltin

import csv  # Import the csv module to handle CSV file operations
import os  # Import the os module to handle environment variables


def quicksort(arr, keys):
    """Sort a list of dictionaries based on multiple keys using quicksort."""
    if len(arr) <= 1:
        return arr  # Base case: if the array has 1 or 0 elements, it's already sorted
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    # Partition the array into three parts: less than, equal to, and greater than the pivot
    left = [x for x in arr if tuple(x[key] for key in keys) < tuple(pivot[key] for key in keys)]
    middle = [x for x in arr if tuple(x[key] for key in keys) == tuple(pivot[key] for key in keys)]
    right = [x for x in arr if tuple(x[key] for key in keys) > tuple(pivot[key] for key in keys)]
    # Recursively sort the left and right parts and concatenate them with the middle part
    return quicksort(left, keys) + middle + quicksort(right, keys)


# Read data from input.txt
input_file = os.getenv('INPUT_FILE_PATH', 'input.txt')  # Get the input file path from environment variable or use default
data = []  # Initialize an empty list to store the data
with open(input_file, 'r') as f:
    reader = csv.DictReader(f)  # Create a CSV reader object to read the file as dictionaries
    for row in reader:
        data.append(row)  # Append each row (dictionary) to the data list

# Sort data by multiple keys
sorted_data = quicksort(data, ['Name', 'Country', 'Ethnicity', 'Job', 'Email'])

# Write sorted data to output.txt
output_file = os.getenv('OUTPUT_FILE_PATH', 'output.txt')  # Get the output file path from environment variable or use default
with open(output_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Name', 'Country', 'Ethnicity', 'Job', 'Email'])
    writer.writeheader()  # Write the header row to the output file
    writer.writerows(sorted_data)  # Write the sorted data to the output file

print("Data sorted and written to output.txt")  # Print a confirmation message