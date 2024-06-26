# Eugene Park
# 2024.05.30
# Appends the date modified of the file to the back of the file in _YYYYMMDD format
# Only files within the direct directory, not any sub directories
# Only for files that do not have the date stamp appeneded in the _YYYYMMDD format

import os
import re
import shutil
from datetime import datetime
from GetPath import *

# Example usage:
#directory_path = "/path/to/directory"  # Replace this with the path to your directory
#append_date_to_filenames(directory_path)

def find_filenames_without_numbers(directory):
    filenames = os.listdir(directory)
    pattern = re.compile(r'^(?!.*_\d{8}).*$')

    filenames_without_numbers = []
    for filename in filenames:
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and pattern.match(filename):
            filenames_without_numbers.append(filename)

    return filenames_without_numbers

def append_date_modified(directory):
    filenames = find_filenames_without_numbers(directory)

    for filename in filenames:
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            modified_time = os.path.getmtime(filepath)
            #modified_date = datetime.datetime.fromtimestamp(modified_time).strftime('%Y%m%d')
            modified_date = datetime.fromtimestamp(modified_time).strftime('%Y%m%d')

            # Split the file name and extension
            file_name_no_ext, file_ext = os.path.splitext(filename)

            # Create the new file name with the date suffix
            new_filename = f"{file_name_no_ext}_{modified_date}{file_ext}"

            new_filepath = os.path.join(directory, new_filename)
            os.rename(filepath, new_filepath)
            print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    file_path = get_file_path()
    print("File path entered:", file_path)

    append_date_modified(file_path)




