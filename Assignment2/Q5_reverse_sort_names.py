#docstring Question 5
"""Sort a list of student names in reverse alphabetical order."""
print(__doc__)
print()

def sort_li(names):
    li1 = sorted(names, reverse=True)
    return li1

details = []
rng = int(input("Enter the number of details you want to input:"))
for i in range(rng):
    name = input("Enter student's name:")
    details.append(name)

final_li = sort_li(details)

print("List in Reverse alphabetical order:")
for n in final_li:
    print(n)