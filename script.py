# Implements a script for sorting and renaming files in a directory
# Uses the argparse module to parse command line arguments for the directory path, random string length, and sorting algorithm
# -p or --path: Required flag, specifies the directory path to process files
# -l or --len: Optional flag, specifies the length of the random string for the new filename, default is 10
# -a or --algorithm: Optional flag, specifies the sorting algorithm to use, either 'bubble' or 'quick', default is 'quick'
# Sorting algorithm can be either bubble sort or quick sort, default is quick sort
# Implements both bubble sort and quick sort functions
# Renames files in the directory by generating a random string, current timestamp, and SHA256 hexadecimal hash of the new filename
# Prints out the number of processed files and the new filename of the last processed file.

import os
import time
import hashlib
import random
import argparse
import sys

# Set up the command line argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', help='Path to your directory', required=True)
parser.add_argument('-l', '--len', help='Length of random string for new filename', default=10, type=int)
parser.add_argument('-a', '--algorithm', help='Sorting algorithm to use (bubble or quick)', default='quick', choices=['bubble', 'quick'])

# Parse the command line arguments
args = parser.parse_args()

path = args.path
length = args.len
algorithm = args.algorithm

# Sort array using bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Partition function for quick sort
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Sort array using quick sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if algorithm == 'bubble':
    arr = [64, 34, 25, 12, 22, 11, 90]
    arr = bubble_sort(arr)
    print(f"Sorted array using bubble sort: {arr}")
else:
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print(f"Sorted array using quick sort: {arr}")

# Renaming files in the directory
print(f"Renaming files in directory: {path}")
total_files = len(os.listdir(path))
count = 0
for i, filename in enumerate(os.listdir(path)):
    print("Processing file {} of {}\r".format(i+1, total_files), end='\r')
    sys.stdout.flush()
    extension = os.path.splitext(filename)[1]
    random_str = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))
    current_time = str(int(time.time()))
    new_file_name = random_str + current_time + extension
    hash_object = hashlib.sha256(new_file_name.encode())
    hex_dig = hash_object.hexdigest()
    new_file_name = hex_dig[:10] + new_file_name
    os.rename(os.path.join(path, filename), os.path.join(path, new_file_name))
    count += 1

# Show the number of processed files
print(f"{count}/{total_files} files processed - {new_file_name}", end='')


