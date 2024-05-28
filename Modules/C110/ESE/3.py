def calcCharge(items): 
    if items == 1:
        shipping_charge = 2.45
    else:
        shipping_charge = (((items - 1) * 1.15) + 2.45)
    return shipping_charge 

items = int(input("Enter number of items:"))
shipping_charge = calcCharge(items)
print("Shipping charge is $",shipping_charge)



