#docstring Question2
"""This program takes student details as input from the user and appends them to an existing
csv file named 'records.csv'. The details include student_name, roll_no, program, year and group.
"""
print(__doc__)
print()
print("Enter the following information:\n")
student_name = input(f'Student Name : ')
roll_no = int(input(f'Roll Number  : '))
program = (input(f'Program      : '))
year = input(f'Year         : ')
grp = input(f'Group        : ')  

import csv
with open("records.csv","a",newline="") as file:
    data = csv.writer(file)
    data.writerow([student_name, roll_no, program, year, grp])

print(f'{student_name} has been added successfully.')