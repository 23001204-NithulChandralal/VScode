#Revision Q10a

def groupPurchases(purchases):
    below100 = []
    above100 = []

    for purchase in purchases:
        if purchase < 100:
            below100.append(purchase)
        else:
            above100.append(purchase)

    return [below100 , above100]

    
