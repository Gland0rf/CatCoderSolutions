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
    
    pointData = content[0].split(" ")
    gameData = content[1].split(" ")
    
    gameCount = int(gameData[0])
    playerCount = int(gameData[1])
    
    winIncrement = int(pointData[0])
    lossDecrement = int(pointData[1])
    
    del content[0:2]
    del content[-1] #Empty Line
    
    playerPoints = {}
    
    for line in content:
        line = line.split(" ")
        playerOneID = int(line[0])
        playerOneScore = int(line[1])
        playerTwoID = int(line[2])
        playerTwoScore = int(line[3])
        
        if playerOneID not in playerPoints:
            playerPoints[playerOneID] = 0
        if playerTwoID not in playerPoints:
                playerPoints[playerTwoID] = 0
            
        #Find Winner
        if playerOneScore > playerTwoScore:
            playerPoints[playerOneID] += winIncrement
            playerPoints[playerTwoID] -= lossDecrement
        else:
            playerPoints[playerOneID] -= lossDecrement
            playerPoints[playerTwoID] += winIncrement
    
    playerPoints = dict(sorted(playerPoints.items(), key=lambda x: (x[1], -x[0]), reverse=True))
    final_str = ""
    for player in playerPoints:
        final_str += f"{player} {playerPoints[player]}\n"
    
    with open(f"./output/output_{x+1}", "w") as f:
        f.write(final_str)
    x += 1
        