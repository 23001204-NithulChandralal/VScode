cumdis = 0 
discount = 0 
lastprice = True 

while lastprice:
    ori = float(input("Enter product price:"))
    discount = round(ori *0.2,2)
    cumdis += round(discount,2)
    discountprice = round(ori - discount,2)
    
    print ("Price:", ori , "Discount Price:", discountprice,"Discount:", discount, "Cumulative Discount:",round(cumdis,2))
    
    if cumdis + discount > 200:
        lastprice = False 
        print ("This purchase has exceeded the cumulative value of $200")
        print("Total discount before exceeding is:", round(cumdis - discount,2))
        break 
    
