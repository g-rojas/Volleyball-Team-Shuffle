import array as team
import random

player_scores = {}

def welcome_message():
    print("\nHello welcome to my Volleyball team generator")

def print_instructions():
        print("\nYou will enter how many players and how Many teams you want. You can Have it randomly generated or you can also input skill and have the teams equally skilled. You will then input each players name. After The teams are chosen You can add or remove players at any given time and reset the teams. You can also re adjust players to the team that you want them in.")

def ask_for_num(prompt):
     while True:
      user_input = input(prompt)
      try:
            user_input = int(user_input)
            return user_input
      except ValueError:
        print("Invalid input!")

def num_within_range(prompt, min_value, max_value):
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def print_first_options():
    print("How would you like to play?")
    print("1. Random players for each team")
    print("2. Teams based on skillset")
        
def ask_for_player_name(num_names):
    names = []
    for i in range(num_names):
        name = input(f"Enter player {i + 1} out of {num_names} name:")
        names.append(name)
       #Print name entered after entering
        for j, name in enumerate(names, start=1):
            print(f"{j}. {name}")
    return names

def random_option(num_teams, num_players, player_names):
    players_per_team = num_players / num_teams
    print(f"Number Players: {num_players} % Number of teams: {num_teams} =")
    print(f"Players per team: {players_per_team}")
    random.shuffle(player_names)
    teams = [[] for _ in range(num_teams)]
    for i, player in enumerate(player_names):
        teams[i % num_teams].append(player)
    #print
    for j in range(num_teams):
        print(f"Team {j + 1}:  {teams[j]}")

def collect_names_to_dict(num_players, num_teams):
    players_per_team = num_players / num_teams
    print(f"Number Players: {num_players} % Number of teams: {num_teams} =")
    print(f"Players per team: {players_per_team}")
    for i in range(num_players):
        name = input("Enter player's name: ")
        player_scores[name] = None
    for name in player_scores:
        print(name)
    return player_scores
    
def assign_player_scores():
    for name in player_scores:
        while True:
            try:
                score = int(input(f"Enter score for {name}: "))
                player_scores[name] = score
                break
            except ValueError:
                print("Please enter a valid number for the score.")
   #print(player_scores.values())
    sorted_ranking = sorted(player_scores.values(), reverse=True)
    print(f"Ranking Sorted: {sorted_ranking}")
   
def skillset_option(num_teams, num_players, player_scores):
        print(player_scores.items())
        scores = []
        for value in player_scores.values():
            #scores.append(player_scores.values)
            scores.append(value)
        print(scores)
       #Assigned scores list with the dictionary values
       #FIXME: sort the list and implement serpetine algorithm