"""
HOMEWORK Q1
a program that converts a grade point value entered by a user to a letter grade. 
"""

gpa = float(input("Enter the grade point value :"))

if gpa > 3.5 and gpa <=4 :
    print("A")
elif gpa >= 2.8 and gpa <= 3.5:
    print("B")
elif gpa >= 2.0 and gpa < 2.8:
    print("c")
elif gpa >= 1.0 and gpa < 2.0:
    print("D")
elif gpa < 1.0 :
    print("F")
else:
    print("GPA entered exceeds the allowable range")