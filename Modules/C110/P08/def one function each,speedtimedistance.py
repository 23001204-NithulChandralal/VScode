"""
Write a program with one function each to calculate distance, speed and time. (i.e. 3 function in total)
"""
def seletection():
    print("D - Distance")
    print("S - Speed")
    print("T - Time")
    print("q -quit")
    choice = input("Enter your choice:")
    while choice != 'D' and choice != 'S' and choice != 'T':
        print("D - Distance")
        print("S - Speed")
        print("T - Time")
        print("q - Quit")
        choice = input("Enter your choice:")
    return choice

def cal_distance():
    s = float(input("Enter Speed:"))
    t = float(input("Enter Time:"))
    distance = s * t
    print("Distance =", round(distance,2))

def cal_speed():
    d = float(input("Enter Distance:"))
    t = float(input("Enter Time:"))
    speed = d / t 
    print("Speed =", round(speed,2))

def cal_time():
    d = float(input("Enter Distance:"))
    s = float(input("Enter Speed:"))
    time = d /s 
    print("Time =", round(time,2))


choice = seletection()
while choice != 'q':
    if choice == "D":
        distance = cal_distance()
    elif choice == "T":
        time = cal_time()
    elif choice == "S":
        speed = cal_speed()
    choice = seletection()
print("The End")

            

