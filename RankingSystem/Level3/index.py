import os

def convertToSec(time):
    timeSplit = time.split(":")
    hours = int(timeSplit[0])
    minutes = int(timeSplit[1])
    seconds = int(timeSplit[2])
    
    seconds += minutes * 60 + hours * 3600
    
    return seconds

def convertToNotation(time):
    hours = str(int(time / 3600))
    time = time % 3600
    minutes = str(int(time / 60))
    time = str(time % 60)
    
    if(len(hours) == 1):
        hours = "0" + hours
    if(len(minutes) == 1):
        minutes = "0" + minutes
    if(len(time) == 1):
        time = "0" + time
    
    finalStr = hours + ":" + minutes + ":" + time
    return finalStr

dir_path = "./input"
files = os.listdir(dir_path)

for file in files:
    splitInput = open(dir_path + "/" + file, "r").read().split(" ")
    
    startTime = convertToSec(splitInput[0])
    submissions = splitInput[1]
    
    submissionList = []
    
    del splitInput[0:2]
    
    for x in range(0, len(splitInput), 3):
        
        uid = splitInput[x]
        timeSubmitted = convertToSec(splitInput[x+1])
        submissionStatus = splitInput[x+2]
        
        if(submissionStatus == "correct"):
            time = (uid, timeSubmitted)
            submissionList.append(time)
       
    sorted_times = sorted(submissionList, key=lambda x: x[1])
    final_str = f"{len(sorted_times)} "
    for submission in sorted_times:
        uid = submission[0]
        timeSubmitted = submission[1]
        
        final_str += f"{uid} {convertToNotation(timeSubmitted)} "
    print(final_str.strip())
        
        