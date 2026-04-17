#docstring Question 4
"""This program reads content from one file and copies it into another file.
The user provides input and output file names. It uses exception handling to
display an error if the input file does not exist or if the output file already exists."""

print(__doc__)
print()

import os
input_file_name = input("Enter the file name to copy its contents:")
output_file_name = input("Enter a new file name to copy the contents into:")

if os.path.exists(output_file_name):
    print("Output file already exists")

else:
    try:
        with open(input_file_name,"r") as file:
            data = file.read()

        with open(output_file_name,"w") as file:
            file.write(data)
        
        print("\nContents copid successfully.")
    except FileNotFoundError:
        print("Input file doesn't exist")
