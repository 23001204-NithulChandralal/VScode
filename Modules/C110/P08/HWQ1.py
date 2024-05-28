"""
HW Q1
1.	Write a function named findMax() to find and return the maximum of three numbers. The three numbers are read from the main program and passed as parameters to findMax(). The main program will print the result returned.
"""

def findMax(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    max_number = findMax(num1, num2, num3)
    print("The maximum number is:", max_number)

main()