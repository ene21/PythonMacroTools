import subprocess

def compare_files(file1, file2):
    winmerge_path = r'C:\Program Files\WinMerge\WinMergeU.exe'  # Path to WinMerge executable
    subprocess.run([winmerge_path, '/e', '/x', '/u', file1, file2])

if __name__ == "__main__":
    file1 = "path_to_your_first_file"
    file2 = "path_to_your_second_file"
    compare_files(file1, file2)