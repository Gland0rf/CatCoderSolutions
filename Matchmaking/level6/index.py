import os
import itertools
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

def find_diff(team_one, team_two, elos):
    dif = 0
    for player in team_one:
        dif += elos[player]
    for player in team_two:
        dif -= elos[player]
        
    return abs(dif)

def find_worse_team(team_a, team_b, elos):
    team_a_rating = 0
    team_b_rating = 0
    for player in team_a:
        team_a_rating += elos[player]
    for player in team_b:
        team_b_rating += elos[player]
    
    return 1 if team_a_rating <= team_b_rating else 2

def find_elo_diff(team_a, team_b, elos):
    worst_elo = -1
    best_elo = -1
    for player in chain(team_a, team_b):
        cur_elo = elos[player]
        
        if worst_elo == -1:
            worst_elo = cur_elo
            best_elo = cur_elo
            
        if cur_elo < worst_elo:
            worst_elo = cur_elo
        if cur_elo > best_elo:
            best_elo = cur_elo
            
    return best_elo - worst_elo

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))

    if r > n:
        return

    yield tuple(pool[i] for i in indices[:r])

    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
        

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
    
    for i in range(0, gameCount):
        line = content[i].split(" ")
        
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
            
        
    #Requeue
    requeue_data = content[gameCount].split(" ")
    maxEloDifference = int(requeue_data[0])
    scoreThreshold = int(requeue_data[1])
    queue_size = int(content[gameCount+1])
    del content[0:gameCount+2]
    
    requeue_player_elos = {}
    
    for player in content:
        player = int(player)
        requeue_player_elos[player] = playerElos[player]
        
    requeue_player_elos = dict(sorted(requeue_player_elos.items(), key=lambda x: (-x[1], x[0])))
    
    requeued_players_raw = sorted(requeue_player_elos, key=lambda x: requeue_player_elos[x], reverse=True)
    
    playerCount = teamSize * 2
    
    should_break = False
    
    final_teams = []
    
    for requeued_players in permutations(requeued_players_raw):
        iter = 0
        teams = []
        for i in range(0, len(requeued_players), playerCount):
            team_a = []
            team_b = []
            
            for j in range(0, playerCount):
                cur_player = requeued_players[iter]
                cur_rating = requeue_player_elos[cur_player]
                if find_worse_team(team_a, team_b, requeue_player_elos) == 1:
                    team_a.append(cur_player)
                else:
                    team_b.append(cur_player)
                iter += 1
            
            teams.append([team_a, team_b])
        
        passed_all = True
        for game in teams:
            team_a = game[0]
            team_b = game[1]
            if find_elo_diff(team_a, team_b, requeue_player_elos) > maxEloDifference:
                passed_all = False
            
            if find_diff(team_a, team_b, playerElos) > scoreThreshold:
                passed_all = False
            
        if passed_all:
            final_teams = teams.copy()
            break
            
        
    """iter = 0
    for i in range(0, len(requeued_players), playerCount):
        
        batch_players = []
        batch_elos = {}
        for player in range(playerCount):
            cur_player = requeued_players[iter]
            batch_elos[cur_player] = requeue_player_elos[cur_player]
            batch_players.append(cur_player)
            
            iter += 1
        
        if abs(list(batch_elos.items())[0][1] - list(batch_elos.items())[-1][1]) > maxEloDifference:
            print("Elo difference too high")
            
        combos = list(itertools.permutations(batch_players))
        for combo in combos:
            team_one = []
            team_two = []
            
            for i in range(teamSize):
                team_one.append(combo[i])
            for i in range(teamSize, teamSize * 2):
                team_two.append(combo[i])
            
            diff = find_diff(team_one, team_two, batch_elos)
            if diff > scoreThreshold:
                print("Diff too high, reshuffling...")
            else:
                
                for player in team_one:
                    final_str += f"{player} "
                for player in team_two:
                    final_str += f"{player} "
                final_str += "\n"
                break"""


    final_str = ""
    for game in final_teams:
        team_a = game[0]
        team_b = game[1]
        
        for player in chain(team_a, team_b):
            final_str += f"{player} "
        final_str += "\n"
        
    print(final_str)
    with open(f"./output/output_{x+1}", "w") as f:
        f.write(final_str)
    x += 1
        