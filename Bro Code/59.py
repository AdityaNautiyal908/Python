# Python file detection

import os

file_path = "C:/Users/Aditya Nautiyal/OneDrive/Desktop/My codes"

if os.path.exists(file_path):
    if os.path.isfile(file_path):
        print("It is a txt file")
    elif os.path.isdir(file_path):
        print("It is a folder")
    else:
        print("Not a txt file")
    print("File exits")
else:
    print("No file found")

