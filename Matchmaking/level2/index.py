import os

def get_data(folder):
    for root, dirs, files in os.walk(folder):
        output = []
        for file in files:
            current_file = os.path.join(root, file)
            with open(current_file, "r") as f:
                output.append(f.read())
    return output

all_content = get_data("./input/")
for x, content in enumerate(all_content):
    content = content.split("\n")
    
    gameData = content[0].split(" ")
    gameCount = int(gameData[0])
    playerCount = int(gameData[1])
    del content[0]
    del content[-1] #Empty Line
    
    playerWins = {}
    
    for line in content:
        line = line.split(" ")
        playerOneID = int(line[0])
        playerOneScore = int(line[1])
        playerTwoID = int(line[2])
        playerTwoScore = int(line[3])
        
        if playerOneID not in playerWins:
            playerWins[playerOneID] = 0
        if playerTwoID not in playerWins:
                playerWins[playerTwoID] = 0
            
        #Find Winner
        if playerOneScore > playerTwoScore:
            playerWins[playerOneID] += 1
        else:
            playerWins[playerTwoID] += 1
    
    playerWins = dict(sorted(playerWins.items(), key=lambda x: (x[1], -x[0]), reverse=True))
    final_str = ""
    for player in playerWins:
        final_str += f"{player} {playerWins[player]}\n"
    
    with open(f"./output/output_{x+1}", "w") as f:
        f.write(final_str)
    x += 1
        