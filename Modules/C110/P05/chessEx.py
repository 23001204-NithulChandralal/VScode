"""
Write a program that reads a position from the user and reports on the color of the sqaure
"""

#input
column = str(input("Emter the column letter :"))
row = int(input("Enter the row number :"))


if column == "a" or column == "c" or column == "e" or column == "g":
    if row == 1 or row == 3 or row == 5 or row == 7:
        print("Black")
    elif row == 2 or row == 4 or row ==  6 or row == 8:  
        print("White")     
elif column == "b" or column == "d" or column == "f" or column == "h":
    if row == 2 or row == 4 or row == 6 or row ==  8:
        print("Black")
    elif row == 1 or row == 3 or row == 5 or row == 7:
        print("White")
