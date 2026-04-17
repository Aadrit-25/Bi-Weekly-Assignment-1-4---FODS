#docstring Question 8
"""Remove duplicates from a list of numbers and return it sorted in ascending order."""
print(__doc__)
print()

def function(numbers):
    return sorted(set(numbers))
nums = []
rng = int(input("Enter the number of details you want to input: "))
for i in range(rng):
    num = int(input("Enter a number:"))
    nums.append(num)

sorted_li = function(nums)
print(f"Final List after removing duplicates and arranging data: {sorted_li}")