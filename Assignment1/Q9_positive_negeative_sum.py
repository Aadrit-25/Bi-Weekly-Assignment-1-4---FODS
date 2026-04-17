#docstring Question 9

'''This program asks user for numbers and finds separate sum of positive and negative numbers until user chooses to exit the program'''

print()
print(__doc__)
print()

p_sum = 0
n_sum = 0

while True:
	print("\n1.Enter a number\n2.Exit")
	opt = int(input("\nSelect an option:"))
	if opt==1:
		num=int(input("Enter a number:"))
		if num>0:
			p_sum+=num
		elif num<0:
			n_sum+=num

	elif opt==2:
		break
	else:
		print("Invalid Input!")
print(f'Sum of positive numbers = {p_sum}')
print(f'Sum of negative numbers = {n_sum}')
			
		
	