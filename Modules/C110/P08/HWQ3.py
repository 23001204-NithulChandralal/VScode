"""
HQ Q3
3.	Write a function called mTable() that can print multiplication tables. The function will accept a multiplicand and the upper-end multiplier as parameters but does not return any result to a calling program or function. The function will assume the base or lower-end multiplier to be 1. The calling program will read the multiplicand and upper-end multiplier and they are passed to the function mTable(). 
For example, for the table printed below, the multiplicand entered is 2 and the upper-end multiplier entered is 4.
"""

def mTable(multiplicand, upper_multiplier):
    # Print the multiplication table
    for multiplier in range(1, upper_multiplier + 1):
        result = multiplicand * multiplier
        print(multiplicand,'x',multiplier, '=' ,result)

# Main program
multiplicand = int(input("Enter the multiplicand: "))
upper_multiplier = int(input("Enter the upper-end multiplier: "))

# Call the mTable() function
mTable(multiplicand, upper_multiplier)