"""
HW Q2
1.	Write a function named findMax() to find and return the maximum of three numbers. The three numbers are read from the main program and passed as parameters to findMax(). The main program will print the result returned.
"""
def findColor(letter, number):
    black_letters = {'a', 'c', 'e', 'g'}
    if letter.lower() in black_letters:
        if int(number) % 2 != 0:
            return 'Black'
        else:
            return 'White'
    else:
        if int(number) % 2 == 0:
            return 'Black'
        else:
            return 'White'

# Main program
letter = input("Enter the letter (a-h), or 'q' to quit: ")
while letter.lower() != 'q':
    number = input("Enter the number (1-8): ")
    color = findColor(letter, number)
    print("The color of",letter,number,"is",color)

    letter = input("Enter the letter (a-h), or 'q' to quit: ")