#input
temp1 = float(input("Enter first temperature :"))
temp2 = float(input("Enter second temperature :"))

#process
av = (temp1 + temp2) / 2 
if av > 37:
    print("See a doctor")
else:
    print("You are fine!")
