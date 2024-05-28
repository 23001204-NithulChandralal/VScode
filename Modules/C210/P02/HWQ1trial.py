print("Sports Table Program")
print("1. Add teams")
print("2. Add Result")
print("3.Exit")

data = {}

choice = input("Please enter choice >")

while choice != "3":
    if choice == "1":
        name = input("Enter name of team >")
        if name in data:
            print("Team already in the list")
        else:
            data[name] = name
    if choice == "2":
        result = input("Please enter the result >")
        result_list = result.split()
        team1 = result_list[0]
        team1score = result_list[1]
        team2score = result_list[3]
        team2 = result_list[4]
        if team1 and team2 in data:
            data[team1].insert([0],"1")
            data[team1].insert([0],"1")
        else:
            print(" One of the Team not added to the list")
        if team1score > team2score:
            data[team1].insert([1],"1")
            data[team2].insert([1],"0")
        else:
            data[team1].insert([1],"0")
            data[team2].insert([1],"1")
        if team1score < team2score:
            data[team1].insert([2],"0")
            data[team2].insert([2],"1")
        else:
            data[team1].insert([2],"1")
            data[team2].insert([2],"0") 
        data[team1].insert([3],team1score)
        data[team2].insert([3],team2score)
    choice = input("Please enter choice >")    

print("Team"                           "Played"   "Won"   "Loss"   "Draw"   "Points")
print("--------------------------------------------------------------------------------")
print(data)
        





for i in data["Teams"]:
    print(i)
            
