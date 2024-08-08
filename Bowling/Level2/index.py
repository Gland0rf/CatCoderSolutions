import os

dir_path = "./input"
files = os.listdir(dir_path)

def check_for_spare(player_score, spareActive):
    if spareActive == True:
        player_score[int(i/2)-1] += throw_1 #Update old shot
        spareActive = False
    return player_score, spareActive

for file in files:
    context = open(dir_path + "/" + file, "r").read().split(":")
    
    amountRound = context[0]
    throws = context[1].split(",")
    
    player_score = []
    spareActive = False
    exit_after_round = False
    
    for i in range(0, len(throws), 2):
        throw_1 = int(throws[i])
        throw_2 = int(throws[i+1])
        throw_3 = 0
        
        #5 -> [1, 1, 2, 3, 4]
        if(i+3 == len(throws)):
            throw_3 = int(throws[i+2])
            exit_after_round = True
        
        final_shot = 0
        raw_shot = throw_1 + throw_2 + throw_3
        final_shot += raw_shot
        
        player_score, spareActive = check_for_spare(player_score, spareActive)
            
        if raw_shot == 10:
            spareActive = True
        
        to_append = final_shot
        if len(player_score) > 0:
            to_append += player_score[int(i/2)-1]
            
        player_score.append(to_append)
        
        if exit_after_round:
            break
        
    with open(f"output/{file.split(".")[0]}.out", "w") as f:
        player_score = [str(x) for x in player_score]
        f.write(",".join(player_score))