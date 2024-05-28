"""
Write a program that allows a user to repeatedly input positive integer numbers but stops at the first entry of a negative number
Extra -
1)enhance the same program to keep count of the number of odd and even numbers entered and display the outcome
2)Enhance the same program further to determine the minimum and maximum of the positive numbers entered and display the outcome
"""
#AsSIGNING
number = int(input("Enter a number:"))
even_num = 0 
odd_num = 0 
maximum = 0 
minimum = 0 

#PROCESS
if number > maximum:                               
    maximum = number
elif number < minimum:
     minimum = number

if number < 0:
      print("Negative number was inputed")
elif number % 2 != 0 :
    odd_num = odd_num + 1 
    print (number,"is Odd")
    print ("Odd #:", odd_num)
else:
     even_num = even_num + 1 
     print(number, " is Even")
     print ("Even #:",even_num)
     
while number > 0 :
    number = int(input("Enter a number:"))
    if number > maximum:
        maximum = number
    elif number < minimum:
         minimum = number

    if number % 2 != 0 :
        odd_num = odd_num + 1 
        print (number,"is Odd")
        print ("Odd #:", odd_num)
    elif number < 0 :
         print("Negative number was inputed")
    else:
        even_num = even_num + 1 
        print(number, " is Even")
        print ("Even #:",even_num)

#OUTPUTS
print ("==========")
print ("Total Odd #:",odd_num)
print ("Total Even #:", even_num)
print ("Minimum #:", minimum)
print ("Maximum #:", maximum)