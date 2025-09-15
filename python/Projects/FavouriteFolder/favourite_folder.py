import os


favourite_folders = [
    r'./favourite/folder1',
    r'./favourite/folder2'
]


input_val = int(input("select which folder starting from index 0:"))

if input_val < len(favourite_folders):
    os.popen(f"explorer {os.path.abspath(favourite_folders[input_val])}")