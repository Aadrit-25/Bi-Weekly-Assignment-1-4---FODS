#docstring Question1
"""This program reads from a CSV file named 'records.csv' and displays its contents.
The fields include student_name, roll_no, program, year, and group.
Each record is read using csv.reader and printed in a formatted way.
"""
print(__doc__)
print()
import csv
with open("records.csv","r") as file:
    line = csv.reader(file)
    next(line)
    for i in line:
        print(f'Student Name : {i[0]}')
        print(f'Roll Number  : {i[1]}')
        print(f'Program      : {i[2]}')
        print(f'Year         : {i[3]}')
        print(f'Group        : {i[4]}\n')  