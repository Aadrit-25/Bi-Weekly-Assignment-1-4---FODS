#docstring Question 5

"""This program reads health data from a CSV file using Pandas
and creates a scattered plot using matplotlib.
It includes plots for weight, height, age, and gender relationships."""

print(__doc__)
print()

import pandas as pd
import matplotlib.pyplot as plt

r = pd.read_csv("health_data.csv")

r['Gender'] = r["Gender"].map({'Male':0, 'Female' :1})
plt.figure()
plt.scatter(r['Weight'],r['Height'])
plt.xlabel("Weight")
plt.ylabel("Height")
plt.title("Weight Vs Height")
plt.show()

plt.figure()
plt.scatter(r['Age'],r['Height'])
plt.xlabel("Age")
plt.ylabel("Height")
plt.title("Age Vs Height")
plt.show()

plt.figure()
plt.scatter(r['Height'],r['Age'])
plt.xlabel("Height")
plt.ylabel("Age")
plt.title("Height Vs Age")
plt.show()

plt.figure()
plt.scatter(r['Gender'],r['Height'])
plt.xlabel("Gender")
plt.ylabel("Height")
plt.title("Gender Vs Height")
plt.show()

plt.figure()
plt.scatter(r['Gender'],r['Weight'])
plt.xlabel("Gender")
plt.ylabel("Weight")
plt.title("Gender Vs Weight")
plt.show()