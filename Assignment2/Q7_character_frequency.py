#docstring Question 7
"""Count the occurrences of each character in a sentence (excluding spaces)."""
print(__doc__)
print()

def key_value(sentence):
    dictionary = {}
    for char in sentence:
        if char!= ' ':
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char]=1
    return dictionary         


sent = input("Enter a sentence:").lower()
result = key_value(sent)

print(f'Input Sentence : {sent}')
for k,v in result.items():
    print(f'{k} occurs {v} times.')