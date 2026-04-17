#docstring Question 4
'''This program takes a single number as input and displays cube, cuberoot, natural log, base 2 log and number raised to power 6 of the input number'''
print()
print(__doc__)
print()

num = int(input("Enter a number:"))
n=1000000000
ln_num = n*(num**(1/n)-1)
ln_b2 = n*(2**(1/n)-1)
print("\n------ Results ------\n")
print(f'I.  Cube of {num} = {num**3}')
print(f'II. Cube root of {num} = {num**(1/3):.2f}')
print(f'III.Natural logarithm of {num} = {ln_num:.2f}')
print(f'IV. Base-2 logarithm of {num} = {ln_num/ln_b2:.2f}')
print(f'V.  {num} raised to the power of 6 = {num**6}')
