#docstring Question 6
"""Search for a country in a list and return its index if found"""
print(__doc__)
print()

def li(countries_list,country_to_find):
        if country_to_find in countries_list:
            return countries_list.index(country_to_find)
        return f'Not found in list'


countries = []
rng = int(input("Enter the number of countries you want to input:"))
for i in range(rng):
    name = input("Enter country's name:")
    countries.append(name)

searched_name = input("Enter a country's name to search its' index:")
result = li(countries,searched_name)

print(f'Index of {searched_name} : {result}')