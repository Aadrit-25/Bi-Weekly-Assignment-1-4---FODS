#docstring Question 6
'''This program displays all prime numbers within a user-defined range and also keeps a count of the numbers along with their sum.'''

print()
print(__doc__)
print()

low_rng = int(input("Enter the lower range:"))
up_rng = int(input("Enter the upper range:"))
s = 0
p_count = 0
for n in range(low_rng,up_rng+1):
	count = 0
	i=1
	while i<=n:
		if n%i==0:
			count +=1
		i+=1
	if count == 2:
		print(n)
		s += n
		p_count+=1
print(f'Prime numbers between {low_rng} and {up_rng} = {p_count}')
print(f'Sum of prime numbers between {low_rng} and {up_rng} = {s}')
		
	


	
