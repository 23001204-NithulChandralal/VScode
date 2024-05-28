"""
Define one function that displays a text based menu and returns a user selected option.
"""

#function selection
def fn_select ():
    choice = input("Enter 'D' for distance,'S' for speed, 'T' for time:")
    while choice != 'D' and choice != 'S' and choice != 'T':
        choice = input("Enter 'D' for distance,'S' for speed, 'T' for time:")
    return choice

choice = fn_select()
if choice == "D":
    speed = float(input("Enter Speed:"))
    time = float(input("Enter Time:"))
    Distance = speed * time
    print("Distance =", Distance)
elif choice == "T":
    distance = float(input("Enter Distance:"))
    speed = float(input("Enter Speed:"))
    time = distance / speed 
    print("Time =", time)
elif choice == "S":
    distance = float(input("Enter Distance:"))
    time = float(input("Enter Time:"))
    speed = distance / time
    print("Speed =", speed)






