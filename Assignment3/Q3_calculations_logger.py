#docstring Question 3
"""This program accepts a list of integers from the user and performs arithmetic operations
such as addition, subtraction, multiplication, and division.
The results are stored in a file along woth the current date and time.
The program continues until the user chooses to exit, after which all stored
results are displayed in a formatted manner."""

print(__doc__)
print()

from datetime import datetime
while True:
    num = input("Enter numbers separated by comma:")
    numbers = [int(x) for x in num.split(",")]

    add = sum(numbers)

    sub = numbers[0]
    for n in numbers[1:]:
        sub -= n
    
    product = 1
    for n in numbers:
        product *= n
        
    div = numbers[0]
    for n in numbers[1:]:
        if n!= 0:
            div /= n
        else:
            div = "Undefined: Division by zero"
            break

    dt = datetime.now()
    timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")

    with open ("results.txt","a") as file:
        file.write(f'Time   :{timestamp}\n')
        file.write(f'Numbers:{numbers}\n')
        file.write(f'Sum    :{add}\n')
        file.write(f"Subtraction:{sub}\n")
        file.write(f'Multiplication :{product}\n')
        file.write(f'Division :{div}\n')
        file.write("-"*20)

        choice = input("Do you want to continue(y/n)? : ").lower()
        if choice!='y':
            break

print("Saved Results successfully")
with open('results.txt','r') as file:
    for line in file:
        print(line,end="")




