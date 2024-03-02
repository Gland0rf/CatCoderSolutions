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
    taskValue = int(splitInput[1])
    submissions = splitInput[2]
    del splitInput[0:3]
    
    submissionList = {}
    taskPoints = {}
    userPoints = {}
    
    for x in range(0, len(splitInput), 4):
        
        uid = splitInput[x]
        timeSubmitted = convertToSec(splitInput[x+1])
        submissionStatus = splitInput[x+2]
        taskID = splitInput[x+3]
        
        time = (uid, timeSubmitted, submissionStatus)
        if(taskID in submissionList):
            submissionList[taskID].append(time)
        else:
            submissionList[taskID] = [time]
           
    """highestValue = -1
    highestUID = -1
    for key in submissionList.keys():
        value = int(submissionList[key])
        if value < highestValue or highestValue == -1:
            highestValue = value
            highestUID = key"""
            
    completedTasksByUsers = {}
    
    for task in submissionList:
        submissions = submissionList[task]
        sorted_times = sorted(submissions, key=lambda x: x[1])
    
        for item in sorted_times:
            uid = int(item[0])
            submissionValue = 0
            submissionStatus = item[2]
            if(submissionStatus == "wrong"):
                submissionValue = 0
            elif task in taskPoints:
                submissionValue = taskPoints[task]
                taskPoints[task] = submissionValue - 1
            else:
                submissionValue = taskValue
                taskPoints[task] = submissionValue - 1
                
            user_already_completed = False
            if(submissionStatus == "correct"):
                if(uid in completedTasksByUsers and submissionStatus):
                    completedTasksByUser = completedTasksByUsers[uid]
                    if(task in completedTasksByUser):
                        user_already_completed = True
                    else:
                        completedTasksByUsers[uid].append(task)
                else:
                    completedTasksByUsers[uid] = [task]
                
                
            if(not user_already_completed):
                if uid in userPoints:
                    userPoints[uid] += submissionValue
                else:
                    userPoints[uid] = submissionValue
                
              
    sorted_points = dict(sorted(userPoints.items(), key=lambda x: (-x[1], x[0])))
    
    finalStr = ""
    for uid in sorted_points:
        finalStr += f"{sorted_points[uid]} {uid} "
        
    print("\n" + finalStr)