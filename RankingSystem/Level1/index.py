import os

def convertToSec(time):
    timeSplit = time.split(":")
    hours = int(timeSplit[0])
    minutes = int(timeSplit[1])
    seconds = int(timeSplit[2])
    
    seconds += minutes * 60 + hours * 3600
    
    return seconds

dir_path = "./input"
files = os.listdir(dir_path)

for file in files:
    splitInput = open(dir_path + "/" + file, "r").read().split(" ")
    
    startTime = convertToSec(splitInput[0])
    endTime = convertToSec(splitInput[1])
    
    timeDif = endTime - startTime
    print(timeDif)