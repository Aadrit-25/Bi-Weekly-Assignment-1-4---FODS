#docstring Question 6
"""This program reads health data from a CSV file and computes
BMI for each record. It also categorizes individuals into different
health status groups based on BMI values."""

print(__doc__)
print()

import pandas as pd

r = pd.read_csv("health_data.csv")

r["Height"] = r["Height"]/100
r["BMI"] = r["Weight"]/r["Height"]

def status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <=24.9:
        return "Healthy"
    elif 25<= bmi <= 29.9:
        return "Overweight risk"
    elif 30<= bmi <=34.9:
        return "High risk of diabetes/ heart disease"
    elif bmi >= 40:
        return "Critical health condition"
    else:
        return "Very high risk"

r["Health_Status"] = r["BMI"].apply(status)

print(r)