#docstring Question 5

'''This program takes the marks of 6 subjects and calculates total, average, percentage, and grade according to the mentioned rules.'''

print()
print(__doc__)
print()

total = 0
marks_dict = {}

for i in range(6):
	sub = input("Enter subject name: ")
	m = float(input(f"Enter marks for {sub}: "))
	if 0>m>100:
		print("Invalid marks! Enter 0-100.")
		break
	marks_dict[sub] = m
	total += m

print("\n------ Marks Obtained ------\n")
for sub, m in marks_dict.items():
	print(f"{sub} : {m}")

avg = total / 6
percentage = (total / 600) * 100
print(f"\nTotal = {total}")
print(f"Average = {avg:.2f}")
print(f"Percentage = {percentage:.2f}%")

if percentage >= 85:
	print("Grade : Distinction")
elif percentage >= 70:
	print("Grade : First Division")
elif percentage >= 55:
	print("Grade : Second Division")
elif percentage >= 45:
	print("Grade : Third Division")
else:
	print("Grade : Fail")







	