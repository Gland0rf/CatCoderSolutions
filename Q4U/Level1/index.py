import os

dir_path = "./input"
files = os.listdir(dir_path)

for file in files:
    content = open(dir_path + "/" + file, "r").read().split(" ")
    
    queue = int(content[0])
    startIndex = int(content[1]) - 1
    endIndex = int(content[2])
    del content[0:3]
    
    #Convert array to ints
    content = [int(x) for x in content]
    
    start_capital = sum(content[startIndex:endIndex])
    
    print(start_capital)