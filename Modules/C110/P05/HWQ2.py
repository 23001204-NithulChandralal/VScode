"""
HW Q2 Write a program to check and display if an individual is allowed to paricipate
"""

name = input("Enter your name:")
age = int(input("Enter your age:"))
gender = input("Enter your gender (M/F):")

if gender == "M":
    if age >= 15:
        print(name,"( age",age,")" "is ALLOWED to participate!")
    else:
        print(name,"( age",age,")" "is NOT ALLOWED to participate!")
elif gender == "F":
    if age >= 17:
        print(name,"( age",age,")" "is ALLOWED to participate!")
    else:
        print(name,"( age",age,")" "is NOT ALLOWED to participate!")    