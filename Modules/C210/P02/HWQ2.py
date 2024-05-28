print("Sports Table Program")
print("1. Add teams")
print("2. Add Result")
print("3. Search Team")
print("4. Print Table")
print("5. Exit")

data = {}  
choice = input("Please enter choice >")

while choice != "5":
    if choice == "1":
        name = input("Enter name of team >")
        if name in data:
            print("Team already in the list")
        else:
            data[name] = {"Played": 0, "Won": 0, "Loss": 0, "Draw": 0, "Points": 0}

    elif choice == "2":
        result = input("Please enter the result (e.g., 'Team1 4 - 3 Team2') >")
        result_list = result.split()
        
        if len(result_list) == 5:
            team1 = result_list[0]
            team1score = int(result_list[1])
            team2score = int(result_list[4])
            team2 = result_list[3]

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
        else:
            print("Invalid result format. Please use 'Team1 score1 - score2 Team2'.")

    elif choice == "3":
        search_team = input("Enter the name of the team to search for >")
        if search_team in data:
            print("Team: " + search_team)
            print("Played: " + str(data[search_team]['Played']))
            print("Won: " + str(data[search_team]['Won']))
            print("Loss: " + str(data[search_team]['Loss']))
            print("Draw: " + str(data[search_team]['Draw']))
            print("Points: " + str(data[search_team]['Points']))
        else:
            print("Team not found in the list")

    elif choice == "4":
        sorted_data = sorted(data.items)
        print("Team\tPlayed\tWon\tLoss\tDraw\tPoints")
        print("-------------------------------------------------------")
        for team, stats in sorted_data:
            team_stats = f"{team}\t{stats['Played']}\t{stats['Won']}\t{stats['Loss']}\t{stats['Draw']}\t{stats['Points']}"
            print(team_stats)

    choice = input("Please enter choice >")

print("-------------------------------------------------------")
