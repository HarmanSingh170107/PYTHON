import os

# Specify the directory path (current directory by default)
directory_path = '/PYTHON FILE LOCATIONS'

# List and print all files and directories in the specified path
for item in os.listdir(directory_path):
    print(item)

