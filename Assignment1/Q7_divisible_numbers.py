#docstring Question 7

'''This program finds all numbers between 1000 and 2500(inclusive) that are divisible by 9 but not by 6. Further the program has been extended such that the user can enter the boundary within which the numbers need to be calculated.'''

print()
print(__doc__)
print()

print("The numbers between 1000 and 2500(inclusive) that are divisible by 9 but not 6 are:")
r=1000
while 2500>=r>=1000:
	if r%9 == 0 and r%6!=0:
		print(r)
	r+=1

while True:
	ch= input(("\nDo you want to enter a boundary(y/n)? :")).lower()
	if ch != 'y':
		break
	
	low_lim = int(input("Enter the starting boundary:"))
	up_lim = int(input("Enter the ending boundary:"))
	
	temp = low_lim
	if low_lim>up_lim:
		break
	while(up_lim>=temp>=low_lim):
		if temp%9==0 and temp%6!=0:
			print(temp)
		temp+=1