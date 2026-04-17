#docstring Question 7
"""This program defines a class 'Staff' to manage employee details such as emp_id, full_name,
address, phone_number, marital_status, dependents, and salary.
Multiple staff records are writeen to a CSV file 'staff.csv', and
the user can view the stored data. Exception handling is used for file operations."""

print(__doc__)
print()

import csv
class Staff:
    def __init__(self,emp_id,full_name,address,phone_number,marital_status,dependents,salary):
        self.emp_id = emp_id
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.marital_status = marital_status
        self.dependents = dependents
        self.salary = salary

    def add_details(self):
        rng = int(input("Enter the number of details you want to input:"))
        for i in range(rng):
            id = int(input("\nEnter employee ID               : "))
            fN = input("Enter full name of the employee : ")
            add = input("Enter the address               : ")
            pN = int(input("Enter the phone number          : "))
            mS = input("Enter the marital status        : ")
            dS = int(input("Enter the no. of dependents     : "))
            Sal = float(input("Enter the salary               : "))

            with open("staff.csv","a",newline = "") as file:
                line = csv.writer(file)
                line.writerow([id,fN,add,pN,mS,dS,Sal])
            print("Details added successfully.")
            
    def show_details(self):
        try:
            with open("staff.csv","r") as file:
                data = csv.reader(file)
                for l in data:
                    print(f"Employee ID   : {l[0]}")
                    print(f"Name          : {l[1]}")
                    print(f"Address       : {l[2]}")
                    print(f"Phone Number  : {l[3]}")
                    print(f"Marital status: {l[4]}")
                    print(f"Dependents    : {l[5]}")
                    print(f"Salary        : £{l[6]}\n")
        except Exception as a:
            print("Error: File not found!")

obj = Staff(0, "", "", "", "", 0, 0)    #constructor
while True:
    print("\n---- Menu -----\n")
    print("1. Add Details")
    print("2. View Details")
    print("3. Exit")

    ch = int(input("Select an option (1-3): "))
    if ch == 1:
        obj.add_details()
    elif ch == 2:
        obj.show_details()
    elif ch == 3:
        break
    else:
        print("Invalid input!")
