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
    
    maxScore = -1
    maxScoreID = -1
    
    for line in content:
        line = line.split(" ")
        playerOneID = int(line[0])
        playerOneScore = int(line[1])
        playerTwoID = int(line[2])
        playerTwoScore = int(line[3])
        
        if maxScore == -1 or playerOneScore > maxScore or (playerOneScore == maxScore and playerOneID < maxScoreID):
            maxScoreID = playerOneID
            maxScore = playerOneScore
        if playerTwoScore > maxScore or (playerTwoScore == maxScore and playerTwoID < maxScoreID):
            maxScoreID = playerTwoID
            maxScore = playerTwoScore
            
    output_str = f"{maxScoreID} {maxScore}"
    
    with open(f"./output/output_{x+1}", "w") as f:
        f.write(output_str)
    x += 1
        