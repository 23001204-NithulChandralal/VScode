

def countLtrDgt(num_string):
    letter = 0
    digit = 0
    stringlist = []
    num_string = int(input("Enter number of strings:"))
    while num_string != 0:
        num_string = num_string - 1
        strings = input("Enter String:")
        stringlist.append(strings)
        for str in stringlist.isalpha:
            letter = letter + 1 
        for str in stringlist.isnumeric:
            digit = digit + 1 
        print("No of letters:", letter)
        print("No of digits:", digit)
    return letter,digit

string = 0 
countLtrDgt(num_string)



