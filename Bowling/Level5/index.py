import os

dir_path = "./input"
files = os.listdir(dir_path)

def check_for_spare(player_score, spareActive, throw_1, round):
    if spareActive == True:
        player_score[round-1] += throw_1 #Update old shot
        spareActive = False
    return player_score, spareActive

def check_for_strike(player_score, strikeActive, total_throw, round):
    if strikeActive == True:
        player_score[round-1] += total_throw #Update old shot
        strikeActive = False
    return player_score, strikeActive


for file in files:
    context = open(dir_path + "/" + file, "r").read().split(":")
    
    amountRounds = int(context[0])
    throws = context[1].split(",")
    
    player_score = []
    spareActive = False
    strikeActive = False
    exit_after_round = False
    
    i = 0
    round = 0
    while i < len(throws):
        #Get throws
        throw_1 = int(throws[i])
        throw_2 = int(throws[i+1])
        throw_3 = 0
        #5 -> [1, 1, 2, 3, 4]
        if(i+3 == len(throws) and round+2 > amountRounds): #Last round
            throw_3 = int(throws[i+2])
            exit_after_round = True
        
        #Calculate total
        raw_shot = throw_1 + throw_2 + throw_3
        
        #Check for strike
        to_throw = raw_shot
        if exit_after_round:
            to_throw = throw_1 + throw_2
        player_score, strikeActive = check_for_strike(player_score, strikeActive, to_throw, round)
        if throw_1 == 10 and not exit_after_round:
            strikeActive = True
            final_shot = 10
            i -= 1 #Strike isn't a set of 2 nums, so we have to subtract 1
        else:
            final_shot = raw_shot
        
        # Check for spare
        player_score, spareActive = check_for_spare(player_score, spareActive, throw_1, round)
        if raw_shot >= 10 and not strikeActive:
            spareActive = True
        
        #Append the score
        to_append = final_shot
        if len(player_score) > 0:
            to_append += player_score[round-1]
            
        player_score.append(to_append)
        
        i += 2
        round += 1
        if exit_after_round:
            break
        
    with open(f"output/{file.split(".")[0]}.out", "w") as f:
        player_score = [str(x) for x in player_score]
        f.write(",".join(player_score))