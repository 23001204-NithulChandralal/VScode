"""
If and else statament to find out if sphere or circle
"""

#input
r = float(input("Enter the radius value:"))
shape = input("Enter 'c' if shape is circle, if not enter s:")

#process
if shape == 'c' :
    area = 3.14159 * (r * r)
    print("The area of circle is :", area )
else:
    volume = (4/3) * 3.14159 * (r * r * r)
    print ("The volume of sphere is:", volume)
    