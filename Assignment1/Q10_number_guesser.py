#docstring Question 10

'''This program generates random number and is a guessing game sample'''

print()
print(__doc__)
print()

import random


while True:
	r_num=random.randint(1,50)
	guess=7
	for attempt in range(1,8):
		num = int(input("\nEnter your guess:"))
		guess-=1
		if num<r_num:
			print("Too Low")
		elif num>r_num:
			print("Too High")
		elif num==r_num:
			print(f'Congratulations! You guessed the number. The number was {r_num}')
			break
		print(f'Remaining Guesses = {guess}')
		if guess == 0:
			print("Better luck next time!")
	
	break


	
