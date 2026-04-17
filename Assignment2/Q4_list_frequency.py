#docstring Question 4
"""Count how many times each number occurs in a list"""
print(__doc__)
print()

def counts(numbers):
    dictionary = {}
    
    for n in numbers:
        if n in dictionary:
            dictionary[n]+=1
        else:
            dictionary[n] = 1
    return dictionary
    
li1 = [1,2,3,4,5]
li2 = [2,4,3,5,1,10]
li3 = [5,6,7,11,9]


for i, li in enumerate([li1,li2,li3],start = 1):
    print(f'\nList {i} : {li}')
    res = counts(li)
    for k,v in res.items():
        print(f'{k} occurs {v} times.')