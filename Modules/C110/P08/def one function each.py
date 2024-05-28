"""
 Write a program with one function each to calculate the area and volume of cones.
"""
def choice1():
    print("a - area")
    print("v - volume")
    print("q - quit")
    choice = input("Enter your selection:")
    while choice != 'a' and choice != 'v' and choice !=  'q':
        print(" a - area")
        print("v - volume")
        print("q - quit")
        choice = input("Enter your selection:")
    return choice
     
def cone_area():
    R = float(input("Enter radius:"))
    g = float(input("Enter slope:"))
    pi = 3.14
    area = pi*R*(g +R)
    print("The area is:",round(area,2))

def cone_volume():
    R = float(input("Enter radius:"))
    h = float(input("Enter height:"))
    pi = 3.14
    volume = 1/3*pi*(R**2) - h 
    print("The volume is:",round(volume,2))      


choice = choice1()
while choice != 'q':
    if choice == "a":
        cone_area()
    elif choice =="v":
        cone_volume()
    choice = choice1()

print("The End")


    



