#Q7 Revision

items = 0 
total_price = 0 
leftover_money = 0 
budget = int(input("Enter your budget for today:"))

while leftover_money >= 0:
    price_of_item = int(input("Enter the price of the item you bought:"))
    if price_of_item == -1:
        break
    else:
        items = items + 1 
        total_price = total_price + price_of_item
        leftover_money = budget - total_price
        print("Item recorded.")


print("Today, you bought",items,"items for $",total_price)
print("You have $",leftover_money,"left.")






