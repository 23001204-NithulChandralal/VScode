#Q3 Revision

age = int(input("age:"))
height = float(input("Height:"))

if height <= 1.2:
    if age <= 12:
        print("Price is $ 4")
    elif age > 12:
        print("Price is $6")
elif height > 1.2:
    if age <= 12:
        print("Price is $ 4")
    elif age > 12 and age < 65:
        print("Price is $8")
    elif age >= 65:
        print("Price is $6")
