#When entering the scores -> Team1 4 - 3 Team2


print("Sports Table Program")
print("1. Add teams")
print("2. Add Result")
print("3. Exit")

data = {}  

choice = input("Please enter choice >")

while choice != "3":
    if choice == "1":
        name = input("Enter name of team >")
        if name in data:
            print("Team already in the list")
        else:
            data[name] = {"Played": 0, "Won": 0, "Loss": 0, "Draw": 0, "Points": 0}

    elif choice == "2":
        result = input("Please enter the result >")
        result_list = result.split()
        team1 = result_list[0]
        team1score = int(result_list[1]) 
        team2score = int(result_list[3])  
        team2 = result_list[4]

        if team1 in data and team2 in data:
            data[team1]["Played"] = data[team1]["Played"] + 1
            data[team2]["Played"] = data[team2]["Played"] + 1

            if team1score > team2score:
                data[team1]["Won"] = data[team1]["Won"] + 1
                data[team2]["Loss"] = data[team2]["Loss"] + 1
                data[team1]["Points"] = data[team1]["Points"] + 3
            elif team1score < team2score:
                data[team2]["Won"] = data[team2]["Won"] + 1
                data[team1]["Loss"] = data[team1]["Loss"] + 1
                data[team2]["Points"] = data[team2]["Points"] + 3
            else:
                data[team1]["Draw"] = data[team1]["Draw"] + 1
                data[team2]["Draw"] = data[team2]["Draw"] + 1
                data[team1]["Points"] = data[team1]["Points"] + 1
                data[team2]["Points"] = data[team2]["Points"] + 1
        else:
            print("One of the teams is not added to the list")

    choice = input("Please enter choice >")

print("Team\tPlayed\tWon\tLoss\tDraw\tPoints")   #Used ChatGPT FOR Line 51 and Line 54 because not sure how to design to make it look nice           
print("-------------------------------------------------------")
for team, stats in data.items():
    print(team + "\t" + str(stats['Played']) + "\t" + str(stats['Won']) + "\t" + str(stats['Loss']) + "\t" + str(stats['Draw']) + "\t" + str(stats['Points']))
print("-------------------------------------------------------")
