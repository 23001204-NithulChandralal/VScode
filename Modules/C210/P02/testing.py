print("Sports Table Program")
print("1. Add Teams")
print("2. Add Result")
print("3. Exit")

data = {
    "Team": [],
    "games_played": [],
    "games_won": [],
    "games_lost": [],
    "games_drawn": [],
    "points_gained": []
}

choice = input("Please enter choice (1, 2, or 3): ")

while choice != "3":
    if choice == "1":
        name = input("Enter name of team: ")
        if name in data["Team"]:
            print("Team already in the list")
        else:
            data["Team"].append(name)
    elif choice == "2":
        result = input("Please enter the result (e.g., Team1 Score-Team2): ")
        if len(result.split()) == 3 and result.split()[1].count('-') == 1:
            team1, score, team2 = result.split()
            score_team1, score_team2 = [int(x) for x in score.split('-')]
            
            # Update team 1 data
            if team1 in data["Team"]:
                data["games_played"][data["Team"].index(team1)] += 1
                data["games_won"][data["Team"].index(team1)] += 1
                data["points_gained"][data["Team"].index(team1)] += 3

            # Update team 2 data
            if team2 in data["Team"]:
                data["games_played"][data["Team"].index(team2)] += 1
                data["games_drawn"][data["Team"].index(team2)] += 1
                data["points_gained"][data["Team"].index(team2)] += 1
        else:
            print("Invalid result entry")
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please choose a valid option (1, 2, or 3).")

# Print the list of teams and their data
print("Team Data:")
for i, team in enumerate(data["Team"]):
    games_played = data["games_played"][i]
    games_won = data["games_won"][i]
    games_drawn = data["games_drawn"][i]
    points_gained = data["points_gained"][i]
    games_lost = games_played - games_won - games_drawn

    print(f"{team}: Played-{games_played}, Won-{games_won}, Lost-{games_lost}, Drawn-{games_drawn}, Points-{points_gained}")
