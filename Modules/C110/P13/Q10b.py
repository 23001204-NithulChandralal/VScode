#Revision Q10b

def groupPurchases(purchases):
    below100 = []
    above100 = []

    for purchase in purchases:
        if purchase < 100:
            below100.append(purchase)
        else:
            above100.append(purchase)

    return [below100, above100]

purchases = []
purchase = float(input("Enter purchase amount (-1 to exit): "))  # Get the initial purchase input

while purchase != -1:
    purchases.append(purchase)  # Add the purchase to the list
    purchase = float(input("Enter purchase amount (-1 to exit): "))  # Get the next purchase input

lists = groupPurchases(purchases)
below100 = lists[0]
above100 = lists[1]

print("Purchases below $100:", below100)
print("Purchases equal to or above $100:", above100)
