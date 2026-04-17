#docstring Question 8

'''This program calculates the factorial of input number and strictly checks whether the number is a valid positive number or not before performing calculations.'''

print()
print(__doc__)
print()
fact = 1
num = int(input("Enter a positive integer to find its' factorial:"))

if num==0:
	print(f'The factorial of {num} is {fact}.')
elif num>0:
	for i in range(1,num+1):
		fact = fact*i
	print(f'The factorial of {num} is {fact}.')
else:
	print("Invalid input! Please enter a positive integer.")

