#docstring Question 1
'''
    Calculates and displays the sum, difference, product, and quotient of two numbers
    
    Parameters:
    num1 (int) : First number
    num1 (int) : Second number
'''
print(__doc__)
print()
def calc(num1,num2):
    print(f'Sum = {num1 + num2}')
    print(f'Difference = {num1 - num2}')
    print(f'Product = {num1*num2}')
    if num2!=0:
        print(f'Quotient = {num1/num2:.2f}')
    else:
        print(f'Quotient = undefined[division by zero]')

a= int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

calc(a,b)