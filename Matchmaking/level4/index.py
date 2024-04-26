import os

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
    

all_content = get_data("./input/")
for x, content in enumerate(all_content):
    content = content.split("\n")
    
    gameData = content[0].split(" ")
    
    gameCount = int(gameData[0])
    playerCount = int(gameData[1])
    
    del content[0:1]
    del content[-1] #Empty Line
    
    playerElo = {}
    
    for line in content:
        line = line.split(" ")
        playerOneID = int(line[0])
        playerOneScore = int(line[1])
        playerTwoID = int(line[2])
        playerTwoScore = int(line[3])
        
        if playerOneID not in playerElo:
            playerElo[playerOneID] = 1000
        if playerTwoID not in playerElo:
            playerElo[playerTwoID] = 1000
            
        old_elo_playerOne = playerElo[playerOneID]
        old_elo_playerTwo = playerElo[playerTwoID]
            
        #Find Winner
        if playerOneScore > playerTwoScore:
            new_elo_playerOne = calc_new_elo(old_elo_playerOne, old_elo_playerTwo, 1)
            new_elo_playerTwo = calc_new_elo(old_elo_playerTwo, old_elo_playerOne, 0)
        else:
            new_elo_playerTwo = calc_new_elo(old_elo_playerTwo, old_elo_playerOne, 1)
            new_elo_playerOne = calc_new_elo(old_elo_playerOne, old_elo_playerTwo, 0)
            
        playerElo[playerOneID] = new_elo_playerOne
        playerElo[playerTwoID] = new_elo_playerTwo
    
    playerElo = dict(sorted(playerElo.items(), key=lambda x: (x[1], -x[0]), reverse=True))
    final_str = ""
    for player in playerElo:
        final_str += f"{player} {playerElo[player]}\n"
    
    with open(f"./output/output_{x+1}", "w") as f:
        f.write(final_str)
    x += 1
        