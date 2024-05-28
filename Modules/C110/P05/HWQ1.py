"""
HW Q1 Correcting all errors 
"""

gender = input("Enter gender: ")
spent = float(input("Enter amount spent: "))

if gender == "male":
    if spent >= 100: 
        print("Shaver")
    else:
        print("None")
elif gender == "female":
    if spent >= 100:
        print("Hand Cream")
    else:
        print("None")