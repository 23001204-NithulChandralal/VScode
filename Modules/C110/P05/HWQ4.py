"""
Write a program to state if a person os eligible for the different attractions in the mini fun fair 
"""

height = int(input("Enter your height:"))
age = int(input("Enter your age:"))

if age < 10:
    if height < 95 :
        print("Eligible for Ferries Wheel")
    elif height >= 95 and height < 120 :
        print("Eligible for Ferries Wheel and Merry-Go-Round")
    elif height >= 120 :
        print("Eligible for Ferris Wheel, Merry-Go-Round and Roller Coaster.")
elif age >= 10:
    if height < 95 :
        print("Eligible for Ferries Wheel")
    elif height >= 95 and height < 120:
        print("Eligible for Ferris Wheel and Merry-Go-Round")
    elif height >= 120 :
        print("Eligible for Ferris Wheel, Merry-Go-Round and Roller Coaster")        