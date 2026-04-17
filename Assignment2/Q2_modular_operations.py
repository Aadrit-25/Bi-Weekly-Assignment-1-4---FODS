#docstring Question 2
"""Perform addition, multiplication, division, floor division and exponentiation on two numbers"""
print(__doc__)
print()

def add(num1,num2):
    return num1+num2
    """Returns the sum of two numbers"""
def product(num1,num2):
    return num1*num2
    """Returns the product of two numbers"""
def div(num1,num2):
    """Returns the division of num1 by num2. Returns none if num2 is zero"""
    if num2!=0:
        return num1/num2
    else:
        return None
def floor_div(num1,num2):
    """Returns the floor division of num1 by num2. Returns none if num2 is zero"""
    if num2!=0:
        return num1//num2
    else:
        return None
def exponential(num1,num2):
    """Returns num1 raised to the power of num2"""
    return num1**num2

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

r1 = div(a,b)
r2 = floor_div(a,b)
print("-----Results-----")
print(f'I.  Addition       : {add(a,b)}')
print(f'II. Multiplication : {product(a,b):.2f}')
if r1 is None:
    print(f'III.Division       : Undefined [Division by zero]')
else:
    print(f'III.Division       : {r1:.2f}')
if r2 is None:
    print(f'IV. Floor Division : Undefined [Division by zero]')
else:
    print(f'IV. Floor Division : {r2:.2f}')
print(f'V.  Exponentiation : {exponential(a,b):.2f}')