"""
Write a program that displays the applicable gifts based on the table.
"""

#input
age = int(input("Enter your age : "))
spend = float(input("Enter your spending : $"))


if age < 21 and age > 12 :
    if spend > 0 and spend < 200 :
        print("No reward")
    elif spend > 200 and spend < 350 :
        print ("A mouse pad")
    else:
        print ("A mouse")
elif age >= 21 and age <= 40 :
    if spend > 100 and spend < 100:
        print ("Jollibee meal")
    elif spend > 200 and spend < 350 :
        print ("Jollibee meal & mouse pad")
    elif spend < 100:
        print ("No reward")
    else:
        print(" 50$ voucher")
elif age > 40:
    if spend > 100 and spend < 100:
        print (" 20$ voucher")
    elif spend > 200 and spend < 350 :
        print ("$30 voucher")
    elif spend < 100:
        print ("No reward")
    else:
        print (" 50$ voucher")
else:
    print ("No reward")
