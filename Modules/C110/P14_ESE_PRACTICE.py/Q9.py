def get_discount(price_list):
    total = 0 
    for price in price_list:
        total = total + price

        if total <= 200:
            discount = len(price_list) * 2 
        else:
            discount = len(price_list) * 4 

        return discount
    
get_discount( [50, 30, 40, 20.5] )
get_discount( [150, 35, 42.9, 60, 75] )
