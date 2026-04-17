#docstring Question 2
"""This program takes a list of at least 12 numbers from user,
sort the list, and perform slicing operations to extract
elements from specified index ranges"""

print(__doc__)
print()

import numpy as np

try:
    n = int(input("How many numbers do you want to enter?:\n"))
    if (n>=12):
        li = []
        for i in range(n):
            val = int(input(f"Enter element {i+1} : "))
            li.append(val)
        
        li.sort()
        print(f"Ordered list in ascending order : {li}")

        print(f"Elements from index 3 to 6 : {li[3:6]}")
        print(f"Elements from index 6 to 9 : {li[6:9]}")
        print(f"Elements from index 4 to 10 : {li[4:10]}\n")

        li.sort(reverse=True)
        print(f"Ordered list in descending order: {li}")
        print(f"Elements from index 3 to 6 : {li[3:6]}")
        print(f"Elements from index 6 to 9 : {li[6:9]}")
        print(f"Elements from index 4 to 10 : {li[4:10]}\n")
    else:
        print("There must be at least 12 inputs.")
except:
    print("Invalid input(s)")