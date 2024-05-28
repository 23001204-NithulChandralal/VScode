def store_birthday(friends_list):
    name = input("Enter friend's name: ")
    birth_month = input("Enter birth month: ")
    friends_list.append([name, birth_month])
    print(name,"'s birthday stored.")

def find_friends_by_month(friends_list):
    month = input("Enter a birth month to find friends: ")
    found_friends = [friend[0] for friend in friends_list if friend[1] == month]
    
    if found_friends:
        print("Friends with birthdays in",month,":", found_friends)
    else:
        print("No friends have birthdays in ",month)

def delete_friend(friends_list):
    name = input("Enter the name of the friend to delete: ")
    for friend in friends_list:
        if friend[0] == name:
            friends_list.remove(friend)
            print(name,"'s data deleted.")
            return
    print(name,"not found in the list.")

def display_menu():
    print("Menu:")
    print("a. Store friend's birthday")
    print("b. Find friends by birth month")
    print("c. Delete friend's data")
    print("d. Quit")

def main():
    friends_list = [['John', 'Dec'], ['Andy', 'Apr'], ['Jane', 'Feb'], ['Cindy', 'Dec'], ['Apple', 'Jan']]
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == 'a':
            store_birthday(friends_list)
        elif choice == 'b':
            find_friends_by_month(friends_list)
        elif choice == 'c':
            delete_friend(friends_list)
        elif choice == 'd':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()
