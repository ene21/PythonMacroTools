import os
import re


def get_file_path():
    file_path = input("Enter the file path: ")
    return file_path

# Regular expression pattern to match _ followed by 8 digits
pattern = re.compile(r'_\d{8}')

def find_files_with_pattern(directory):
    # Traverse directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if file name matches the pattern
            if pattern.search(file):
                # Print the file name
                print(file)

# Change '.' to the directory path you want to search in
directory_to_search = get_file_path()
find_files_with_pattern(directory_to_search)