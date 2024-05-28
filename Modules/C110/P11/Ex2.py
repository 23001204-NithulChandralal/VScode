"""
Write a Singapore Identification Card (IC) checking program.
"""
ic = input("Enter the Singapore IC: ")


if len(ic) == 9:
    if ic[0].isalpha() and ic[-1].isalpha():
        if ic[1:-1].isdigit():
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")
