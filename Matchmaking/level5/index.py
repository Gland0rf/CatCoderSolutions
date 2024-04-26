import os
from itertools import chain

def get_data(folder):
    for root, dirs, files in os.walk(folder):
        output = []
        for file in files:
            current_file = os.path.join(root, file)
            with open(current_file, "r") as f:
                output.append(f.read())
    return output

def calc_winning_chance_of_against(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

def calc_new_elo(player_elo, opponent_elo, outcome, K=32):
    return int(player_elo + K * (outcome - calc_winning_chance_of_against(player_elo, opponent_elo)))

def find_opponent_elo_of(player_to_find, team_a, team_b, elos):
    opponent_elo = 0
    for player in team_b:
        player_elo = elos[player]
        opponent_elo += player_elo
    
    for player in team_a:
        if player != player_to_find:
            player_elo = elos[player]
            opponent_elo -= player_elo
        
    return opponent_elo
        
    

all_content = get_data("./input/")
for x, content in enumerate(all_content):
    content = content.split("\n")
    
    gameData = content[0].split(" ")
    
    gameCount = int(gameData[0])
    playerCount = int(gameData[1])
    teamSize = int(gameData[2])
    
    del content[0]
    del content[-1] #Empty Line
    
    playerElos = {}
    splitIndex = int(len(content[0].split(" ")) / 2)
    
    for line in content:
        line = line.split(" ")
        
        score_teamOne = 0
        score_teamTwo = 0
        players_teamOne = []
        players_teamTwo = []
        
        for i in range(0, splitIndex, 2):
            playerID = int(line[i])
            playerScore = int(line[i+1])
            players_teamOne.append(playerID)
            score_teamOne += playerScore
            
        for i in range(splitIndex, len(line)-1, 2):
            playerID = int(line[i])
            playerScore = int(line[i+1])
            players_teamTwo.append(playerID)
            score_teamTwo += playerScore
            
        for player in chain(players_teamOne, players_teamTwo):
            if player not in playerElos:
                playerElos[player] = 1000
                
        temp_elos = playerElos.copy()
            
        for player in players_teamOne:
            opponent_elo = find_opponent_elo_of(player, players_teamOne, players_teamTwo, temp_elos)
            new_elo = calc_new_elo(temp_elos[player], opponent_elo, score_teamOne > score_teamTwo)
            playerElos[player] = new_elo
        for player in players_teamTwo:
            opponent_elo = find_opponent_elo_of(player, players_teamTwo, players_teamOne, temp_elos)
            new_elo = calc_new_elo(temp_elos[player], opponent_elo, score_teamTwo > score_teamOne)
            playerElos[player] = new_elo
            
    playerElos = dict(sorted(playerElos.items(), key=lambda x: (x[1], -x[0]), reverse=True))
    final_str = ""
    for player in playerElos:
        final_str += f"{player} {playerElos[player]}\n"
    
    with open(f"./output/output_{x+1}", "w") as f:
        f.write(final_str)
    x += 1
        