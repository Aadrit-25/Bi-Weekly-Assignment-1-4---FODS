#docstring Question 3

"""This program generates a NumPy array of random integers,
sort the array, and reshape it into a matrix of valid dimensions using reshape() method"""

print(__doc__)
print()

import numpy as np

try:
    li = np.random.randint(1,20,12)
    print(f"Unsorted List : {li}")
    li.sort()
    print(f"Sorted List : {li}")
    
    li = li.reshape(3,4)
    print(li)

except ValueError:
    print("Invalid dimensions!")