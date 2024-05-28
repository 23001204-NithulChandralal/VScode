onecount = 0 
string = input("Enter 8-character string:")

if len(string) != 8:
    print("the string is not 8 characters long")
elif string != 1 and string != 0:
    print("The string has other characters than 0's and 1's")
else:
    for str in string:
        if str == 1:
            onecount = onecount + 1 
            if onecount % 2 == 0:
                print("Zero (0)")
            else:
                print("One (1)")








