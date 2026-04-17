#docstring Question 3
'''This program takes input from user and determines whether the number is positive, even, positive odd, negative, or negative odd.'''
print()
print(__doc__)
print()
num = int(input("Enter a number:"))

if num>0:
	if num%2==0:
		print(f'{num} is positive even.')
	else:
		print(f'{num} is positive odd.')
elif num<0:
	if num%2!=0:
		print(f'{num} is negative odd.')
	else:
		print(f'{num} is negative even.')
else:
	print("Invalid input! Please Enter a valid input.")
	