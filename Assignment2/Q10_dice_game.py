#docstring Question 10
"""Dice Guessing Game:
- Dice calues range from 1 to 6.
- Player guesses the dice value.
- Show 😊 if guess is correct.
- Show 😐 if guess is off by 1.
- Show dice value if guess is incorrect."""

print(__doc__)
print()
import random
dice = random.randint(1,6)
guess = int(input("Enter your guess:"))

if 0<guess<7:
    if guess == dice:
        print("😊")
    elif abs(guess- dice) == 1:
        print("😐")
    else:
        print(f"GameOver! The value was {dice}")
else:
    print("Invalid Input! Enter a valid guess")