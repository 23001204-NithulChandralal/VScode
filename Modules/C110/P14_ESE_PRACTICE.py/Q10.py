def get_discount(price_list):
    total = 0 
    for price in price_list:
        total = total + price

        if total <= 200:
            discount = len(price_list) * 2 
        else:
            discount = len(price_list) * 4 

        return discount
    



price_list = []
price = int(input("Enter the price of item ( -1 to exit) :"))
price_list.append(price)

while price != -1:
    price = int(input("Enter the price of item (-1 to exit):"))
    price_list.append(price)

price_list.pop()
total_discount = get_discount(price_list) * len(price_list)
print(total_discount)