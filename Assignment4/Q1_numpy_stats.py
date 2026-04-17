#docstring Question1
"""This program generates a Numpy array of
numbers and performs calculations like sum,
mean, maximum and minimum"""

print(__doc__)
print()

import numpy as np

array = np.arange(10,60,10)

total = np.sum(array)

mean = np.mean(array)

largest = np.max(array)
smallest = np.min(array)

print("---- Results ----")
print(f'Total = {total}')
print(f'Mean = {mean}')
print(f'Largest value = {largest}')
print(f'Smallest value = {smallest}')