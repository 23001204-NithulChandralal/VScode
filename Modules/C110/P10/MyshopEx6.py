"""
Assume you are going shopping at MyShop!
Write a program that simulates a paper Shopping List. 
"""
shopping_list = []

def display_menu():
    print("==== Shopping List Menu ====")
    print("1. Add item to the list")
    print("2. Remove item from the list")
    print("3. Count outstanding items")
    print("4. Exit")
    print("============================")

def add_item(item):
    if item in shopping_list:
        print("Item already added to the list.")
    else:
        shopping_list.append(item)
        print("Item added to the list.")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print("Item removed from the list.")
    else:
        print("Item not found in the list.")

def count_items():
    count = len(shopping_list)
    print("Number of outstanding items:", count)


while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == "2":
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == "3":
        count_items()
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
