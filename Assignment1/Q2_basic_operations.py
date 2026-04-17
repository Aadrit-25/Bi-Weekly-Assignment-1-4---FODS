#docstring Question 2

'''This program takes two integer inputs from user and displays the results of addition, multiplication, division, modulus(remainder) and exponentiation in a respective order.'''
print(__doc__)
print()
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number:"))

print("\n------- Results -------\n")
print(f'I.  Addition = {num1+num2}')
print(f'II. Multiplication = {num1*num2}')
print(f'III.Division = {num1/num2:.2f}')
print(f'IV. Modulus (remainder) = {num1%num2}')
print(f'V.  Exponentiation = {num1**num2}')


