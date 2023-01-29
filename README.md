# File Renamer and Sorter

This script provides the functionality to sort arrays using either bubble or quick sort, and to rename files in a directory using a random string and current timestamp.

## Requirements
- Python 3.x
- hashlib module
- random module
- argparse module
- sys module
- time module
- os module

## Command Line Arguments
The following command line arguments are available for use:

- `-p` or `--path`: Path to your directory. Required argument.
- `-l` or `--len`: Length of random string for new filename. Optional argument, default is 10, type is int.
- `-a` or `--algorithm`: Sorting algorithm to use. Optional argument, default is 'quick', choices are 'bubble' or 'quick'.

## Sorting Algorithms
The script provides two sorting algorithms:

- Bubble Sort
- Quick Sort

## Renaming Files
The script renames all files in the provided directory by appending a random string and the current timestamp to the original file name. The new file name is then hashed using the SHA-256 algorithm, and the first 10 characters of the hash are used as a prefix for the new file name.

## Usage
To run the script, simply provide the path to the directory you wish to rename files in, along with any optional arguments.

Example usage:
`python script.py [-h] [-p PATH] [-l LEN] [-a ALGORITHM]`

## Notes
- The script is set up to sort a fixed array and the sorting algorithm can be changed using the -a flag.
- The script renames all files in the specified directory and is not limited to a specific file type.
