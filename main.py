import volleyball

volleyball.welcome_message()

volleyball.print_instructions()

player_count = volleyball.ask_for_num("Enter the number of players: ")
player_count = str(player_count)
print("Player count: " + player_count)
player_count =  int(player_count)

team_count = volleyball.ask_for_num("Enter your team count: ")
team_count = str(team_count)
print("Team count: " + team_count)
team_count = int(team_count)

volleyball.print_first_options()
user_input = volleyball.num_within_range("Enter the number option you want: ",1 ,2)

if user_input == 1:
    print("You have chosen picking teams randomly")
    player_names = volleyball.ask_for_player_name(player_count)
    volleyball.random_option(team_count, player_count, player_names)
else:
    print("You have chosen picking teams based on skill level")
    volleyball.collect_names_to_dict(player_count, team_count)
    volleyball.assign_player_scores()



