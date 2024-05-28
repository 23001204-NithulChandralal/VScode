"""
Demo #1
"""
price = []
item_price = float(input("Item price: $ "))
while item_price != 0:
    price.append(item_price)
    item_price = float(input("Item price: $ "))

print()
for item_price in price:
    print("Item price: $", item_price)
    if item_price > 30.00:
        discounted_price = item_price * 0.75
        print("New price: $",discounted_price)
    else:
        print("No discount offered")
    print()
