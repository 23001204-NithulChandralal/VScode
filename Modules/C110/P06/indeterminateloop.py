"""
 Write a program to sum the numbers entered by a user. The program will display the sum after each number. The programs tops as soon as the sum exceed 200
"""


total = 0  
while total < 200:
    number = int(input("Enter a number:"))
    print(number)
    total = total + number

print("Sum is",total,"and has exceeded 200")