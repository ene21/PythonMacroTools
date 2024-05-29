import os
import shutil
from datetime import datetime

def append_date_to_filenames(directory):
    # Get the current date in YYYYMMDD format
    date_suffix = datetime.now().strftime("%Y%m%d")

    # List all files in the directory
    files = os.listdir(directory)

    # Iterate over each file
    for file_name in files:
        # Check if the entry is a file
        if os.path.isfile(os.path.join(directory, file_name)):
            # Split the file name and extension
            file_name_no_ext, file_ext = os.path.splitext(file_name)

            # Create the new file name with the date suffix
            new_file_name = f"{file_name_no_ext}_{date_suffix}{file_ext}"

            # Rename the file
            os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))

            print(f"Renamed '{file_name}' to '{new_file_name}'")

# Example usage:
#directory_path = "/path/to/directory"  # Replace this with the path to your directory
#append_date_to_filenames(directory_path)
            
def get_file_path():
    file_path = input("Enter the file path: ")
    return file_path

if __name__ == "__main__":
    file_path = get_file_path()
    print("File path entered:", file_path)

    append_date_to_filenames(file_path)


