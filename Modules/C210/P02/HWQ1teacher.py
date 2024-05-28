def display_result(fc_dict):
    print('%-20s %-10s %-10s %-10s %-10s %-10s' % ('Team', 'Played', 'Won', 'Loss', 'Draw', 'Points'))
    print('-'* 70)
    for team in fc_dict:
        stats = fc_dict[team]
        print('%-20s %-10d %-10d %-10d %-10d %-10d' % (team, stats[0], stats[1], stats[2], stats[3], stats[4]))
    print('-' * 70)

def get_opt():
    print("Sports Table Program")
    print("1. Add Teams")
    print("2. Add Result")
    print("3. Exit")
    user_input = int(input("Please enter choice: "))
    return user_input

def add_team(fc_dict):
    team_name= input("enter name of team:")
    if team_name in fc_dict:
        print(team_name, "entered exist")
    elif len(team_name)== 0:
        print("invalid entry")
    else:
        print(team_name, "added")
        print("")
 
    fc_dict[team_name]= [0,0,0,0,0]

def add_result(fc_dict):
    result = input("Please enter the result >")
    result_list = result.split()
    team1 = result_list[0]
    team1score = (result_list[1].split('-')[0]) 
    team2score = (result_list[1].split('-')[1])  
    team2 = result_list[2]

    if team1score > team2score:
        print("Team 1 win")
        fc_dict[team1][0] = fc_dict[team1][0] + 1
        fc_dict[team1][1] = fc_dict[team1][1] + 1
        fc_dict[team1][4] = fc_dict[team1][4] + 3

        fc_dict[team2][0] = fc_dict[team2][0] + 1
        fc_dict[team2][2] = fc_dict[team2][2] + 1     
    elif team1score < team2score:
        print("Team 2 win")
        fc_dict[team2][0] = fc_dict[team2][0] + 1
        fc_dict[team2][1] = fc_dict[team2][1] + 1
        fc_dict[team2][4] = fc_dict[team2][4] + 3  

        fc_dict[team1][0] = fc_dict[team1][0] + 1
        fc_dict[team1][2] = fc_dict[team1][2] + 1    
    else:
        print("Draw")
        fc_dict[team1][0] = fc_dict[team1][0] + 1
        fc_dict[team1][3] = fc_dict[team1][3] + 1
        fc_dict[team1][4] = fc_dict[team1][4] + 1

        fc_dict[team2][0] = fc_dict[team2][0] + 1
        fc_dict[team2][3] = fc_dict[team2][3] + 1
        fc_dict[team2][4] = fc_dict[team2][4] + 1   


fc_dict = {
    "Chelsea":[0,0,0,0,0,],
    "Liverpool":[0,0,0,0,0]
}

user_opt = get_opt()
while user_opt != 3:
    if user_opt == 1:
        add_team(fc_dict)
    elif user_opt == 2:
        add_result(fc_dict)        
    else:
        print("Invalid Option")    
    user_opt = get_opt()
display_result(fc_dict)