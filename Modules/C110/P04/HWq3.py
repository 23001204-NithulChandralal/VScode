"""
HOMEWORK Q3
a program that reads the lengths of 3 sides of a triangle from a user and display a message indicating the type of the triangle.
"""

a = float(input("Enter the length of 1st side:"))
b = float(input("Enter the length of 2nd side:"))
c = float(input("Enter the length of 3rd side:"))

if a == b == c:
    print("equilateral triangle ")
elif a == b or b == c or c == a:
    print("isosceles triangle")
else:
    print ("triangle is scalene")