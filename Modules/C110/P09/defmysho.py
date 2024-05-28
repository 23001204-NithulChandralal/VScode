"""
Ex 3# 
a program was written for MyShop to display the applicable gifts that members will receive based on their age and spending on their platform. 
 Convert the program on one using functions
"""

def twentyone2twelve ():
    if spend > 0 and spend < 200 :
        print("No reward")
    elif spend > 200 and spend < 350 :
        print ("A mouse pad")
    else:
        print ("A mouse")

def twentyone2fourty ():
    if spend > 100 and spend < 100:
        print ("Jollibee meal")
    elif spend > 200 and spend < 350 :
        print ("Jollibee meal & mouse pad")
    elif spend < 100:
        print ("No reward")
    else:
        print(" 50$ voucher")

def morethanfourty ():
    if spend > 100 and spend < 200:
        print (" 20$ voucher")
    elif spend > 200 and spend < 350 :
        print ("$30 voucher")
    elif spend < 100:
        print ("No reward")
    else:
        print (" 50$ voucher") 

#main program
age = int(input("Enter your age : "))
spend = float(input("Enter your spending : $"))

if age < 21 and age > 12 :
    twentyone2twelve ()
elif age >= 21 and age <= 40 :
    twentyone2fourty ()
elif age > 40:
    morethanfourty ()
else:
    print ("No reward")







