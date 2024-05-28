footballteam = {}
choice = input("Please enter choice >")

while choice != "3":
    if choice == "1":
        name = input("Enter name of team >")
        if name in footballteam:
            print("Team already in the list")
        else:
            footballteam[name] = 0  # You can set the value to 0 for now, or any other default value you prefer
    choice = input("Please enter choice >")

# To print the teams in the dictionary, you can iterate through the keys:
for team in footballteam:
    print(team)
