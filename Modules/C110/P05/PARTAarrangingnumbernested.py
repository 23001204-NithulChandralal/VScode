"""
Write a program that reads 3 integer values
a) determine if the numbers are ascending, descending or neither
b) orders and displays the numbers is ascending order
"""

#input
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))

#PART A 
if num1 < num2:
    if num2 < num3:
        print("ascending order")
    else:
        print("neither")
elif num1 > num2:
    if num2 > num3:
        print("descending order")
    else:
        print("neither")
else:
    print("neither")
    
#PART B   
if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
            print( num1, num2, num3 , ".   The smallest of the 3 numbers is",num1,   ",  The largest of the 3 number is" ,num3 )
    else:
            print( num1, num3, num2,".    The smallest of the 3 numbers is",num1,   ",  The largest of the 3 number is" ,num2 )
elif num2 <= num1 and num2 <= num3: 
    if num1 <= num3:
        print(num2, num1, num3,".      The smallest of the 3 numbers is",num2,    ",  The largest of the 3 number is" ,num3)
    else:
        print(num2, num3, num1 ,".     The smallest of the 3 numbers is", num2,    ",  The largest of the 3 number is" ,num3 )
else:
    if num1 <= num2:
        print(num3, num1, num2, ".     The smallest of the 3 numbers is",num3,    ",  The largest of the 3 number is" ,num2)
    else:
        print(num3, num2, num1, ".    The smallest of the 3 numbers is",num3 ,   ",  The largest of the 3 number is" ,num1 )

