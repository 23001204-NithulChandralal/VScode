"""
HW Q3 Write a program that determines if a bank customer qualifies for a personal loan
"""

salary = float(input("Enter salary per annum:$"))
experience = int(input("Years of employment:"))

if salary >= 45000:
    if experience > 3:
        print("Customer is QUALIFIED")
    else:
        print("Customer is NOT QUALIFIED")
else:
    print("Customer NOT QUALIFIED")