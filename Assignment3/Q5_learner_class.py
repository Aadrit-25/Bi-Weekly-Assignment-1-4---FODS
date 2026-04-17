#docstring Question 5
"""This program defines a class 'Learner' with attributes such as roll number,
full name, address, enrollment year, program, and group. An object of the class
is created using user input, and the details are displayed."""

print(__doc__)
print()

class Learner:
    def __init__(self, roll_no, full_name, address, enrollment_year, program, group):
        self.roll_no = roll_no
        self.full_name = full_name
        self.address = address
        self.enrollment_year = enrollment_year
        self.program = program
        self.group = group

    def display(self):
        print("\nDetails:")
        print(f"Roll Number     : {self.roll_no}")
        print(f"Full Name       : {self.full_name}")
        print(f"Address         : {self.address}")
        print(f"Enrollment year : {self.enrollment_year}")
        print(f"Program         : {self.program}")
        print(f"Group           : {self.group}")
    
print("Enter Details:")
roll_no = int(input("Enter roll number:"))
full_name = input("Enter full name:")
address = input("Enter address :")
enrollment_year = int(input("Enter enrollment year:"))
program = input("Enter program :")
group = input("Enter group :")

val = Learner(roll_no, full_name, address, enrollment_year, program, group)

val.display()