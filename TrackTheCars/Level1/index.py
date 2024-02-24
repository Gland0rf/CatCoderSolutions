import os
import math
from shapely.geometry import Point, Polygon

dir_path = "./input"
files = os.listdir(dir_path)

for file in files:
    content = open(dir_path + "/" + file, "r").read().split("\n")
    #LEVEL 1 // 3
    firstRectangle = content[0].split(",")
    amountPositions = int(content[1])
    del content[0:2]
    
    northBorder = float(firstRectangle[0])
    eastBorder = float(firstRectangle[1])
    southBorder = float(firstRectangle[2])
    westBorder = float(firstRectangle[3])
    
    amountCarsFound = 0
    
    for car in content:
        if(car != ""):
            car = car.split(",")
            latitude = float(car[0])
            longitude = float(car[1])
            #Check if in boundaries
            
            if(southBorder < latitude < northBorder and westBorder < longitude < eastBorder):
                amountCarsFound += 1
                
    
    print(amountCarsFound)