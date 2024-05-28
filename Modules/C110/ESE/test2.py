#(a)
def countLtrDgt(s):
    ltrs = 0
    digts = 0
    for char in s:
        if char.isalpha():
            ltrs = ltrs + 1
        elif char.isdigit():
            digts = digts + 1
    print("No of letters:",ltrs)
    print("No of digits:",digts)
    return [ltrs, digts]

#(b)
num_string = int(input("Enter number of strings:"))
while num_string != 0:
    num_string = num_string - 1
    s = input("Enter String:")
    s = countLtrDgt(s)
