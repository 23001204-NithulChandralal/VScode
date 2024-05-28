"""
Write a program that reads a year from the user and displays a messageomdocatomg whether or not its a leap year
"""

#input
year = int(input("Year :"))

#calculation
testyear1 = year % 400 
testyear2 = testyear1 % 100
testyear3 = testyear2 % 4 
#process

if year > 0 :
    if testyear1 == 0:
        print("Leap year")
    elif testyear2 == 0:
        print("Not a leap year ")
    elif testyear3 % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
else:
    print ("Negative year? ERROR")

  

    
    