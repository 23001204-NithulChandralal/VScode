"""
To check if number is odd or even, is negative number else display error 
"""

#input
num = int(input("Enter a number:"))

#process
if num > 0:    #postive
     
#check if odd or even
     if num % 2 == 0:
        print("Even number")
     else:
        print("Odd number")
    
else:
    print ("You have entered a negative number")