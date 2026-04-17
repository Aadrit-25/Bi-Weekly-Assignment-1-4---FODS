#docstring Question 4
"""This program takes two matrices as input and performs
matrix operations such as addition, subtraction, and multiplication
using Numpy.

It also checks for dimension compatibility before performing operations."""

print(__doc__)
print()

import numpy as np

try:
    print("For matrix A :")
    row1 = int(input("Enter the number of rows    : "))
    col1 = int(input("Enter the number of columns : "))

    total1 = row1*col1

    matA = []
    for i in range(total1):
        valA = int(input(f"Enter element {i+1} : "))
        matA.append(valA)
    matA = np.array(matA)
    matA = matA.reshape(row1, col1)

    print("For matrix B:")
    row2 = int(input("Enter the number of rows    : "))
    col2 = int(input("Enter the number of columns : "))

    total2 = row2*col2

    matB = []
    for i in range(total2):
        valB = int(input(f"Enter element {i+1} : "))
        matB.append(valB)
    matB = np.array(matB)
    matB = matB.reshape(row2, col2)

    if row1 == row2 and col1 == col2 :
        matC = matA + matB
        matD = matA - matB
        print("Matrix A:")
        for row in matA:
            for val in row:
                print(val, end=" ")
            print()
        print("Matrix B:")
        for row in matB:
            for val in row:
                print(val, end=" ")
            print()
        print("Sum:")
        for row in matC:
            for val in row:
                print(val, end=" ")
            print()
        print("Difference:")
        for row in matD:
            for val in row:
                print(val, end=" ")
            print()

    if col1 == row2:
        print("Multiplication:")
        matE = np.dot(matA,matB)
        for row in matE:
            for val in row:
                print(val, end=" ")
            print()
    else:
        print("Conditions not valid to perform multiplication")
except ValueError:
    print("Invalid input or dimensions!")