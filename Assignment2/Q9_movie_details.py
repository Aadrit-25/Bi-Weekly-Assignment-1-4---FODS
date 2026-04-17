#docstring Question 9
"""Accepts details of 3 movies (title, director, release year, rating),
store them in dictionaries, and display them in a well-formatted manner."""
print(__doc__)
print()


m = []
for i in range(3):
    title = input("Enter the title of the movie: ")
    direct_name = input("Enter the name of the director: ")
    r_year = int(input("Enter the release year: "))
    rate = float(input("Enter the ratings of the movie: "))

    movies = {
    "Title" : title,
    "Director" : direct_name,
    "Release year" : r_year,
    "Rating" : rate
    }

    m.append(movies)

for i,movie in enumerate(m, start = 1):
    print(f'\nMovie {i}:')
    print(f"Title        : {movie['Title']}")
    print(f"Director     : {movie['Director']}")
    print(f"Release year : {movie['Release year']}")
    print(f"Ratings      : {movie['Rating']}")
    print("-" *15)
