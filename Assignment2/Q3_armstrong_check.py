#docstring Question 3
"""Check whether a given number is armstrong or not"""
print(__doc__)
print()

def armstrong(num_string):
    if not num_string.isdigit():
        return f'Invalid Input! Enter a numeric value.'
    num = int(num_string)
    power = len(num_string)
    total = 0

    for count in num_string:
        total += int(count) ** power
    
    if total == num:
        return f'{num_string} is armstrong.'
    else:
        return f'{num_string} is not armstrong.'

num_s = input("Enter a numeric value:")
result = armstrong(num_s)
print(result)