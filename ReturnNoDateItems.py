#Eugene Park
#31/05/2024
#python script to return me filename in directory that do not contain _ followed by 8 numbers

import os
import re


def get_file_path():
    file_path = input("Enter the file path: ")
    return file_path

def find_filenames_without_numbers(directory):
    filenames = os.listdir(directory)
    pattern = re.compile(r'^[^_]*$|^((?!_)\w)+(?<!\d)(?<!_)$')

    filenames_without_numbers = []
    for filename in filenames:
        if pattern.match(filename):
            filenames_without_numbers.append(filename)

    return filenames_without_numbers

directory_path = get_file_path()
filenames = find_filenames_without_numbers(directory_path)
print("Filenames without _ followed by 8 numbers:")
for filename in filenames:
    print(filename)