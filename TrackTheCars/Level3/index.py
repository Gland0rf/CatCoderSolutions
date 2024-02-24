import os
import math
from shapely.geometry import Point, Polygon

dir_path = "./input"
files = os.listdir(dir_path)

def is_inside_polygon(point, polygon_coords):
    point = Point(point)
    
    polygon = Polygon(polygon_coords)
    
    return polygon.contains(point)

def is_time_in_range(hours, minutes, seconds, start_time, end_time):
    # Convert input time to total seconds
    input_seconds = hours * 3600 + minutes * 60 + seconds

    # Convert start and end times to total seconds
    start_seconds = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]
    end_seconds = end_time[0] * 3600 + end_time[1] * 60 + end_time[2]

    # Check if the input time is within the range
    return start_seconds < input_seconds < end_seconds

    

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
    
    carsInRect = []
    
    for carSpotted in content:
        if(carSpotted != ""):
            carSpotted = carSpotted.split(",")
            identity = carSpotted[0]
            time = carSpotted[1]
            latitude = float(carSpotted[2])
            longitude = float(carSpotted[3])
            #Check if in boundaries
            
            if(southBorder < latitude < northBorder and westBorder < longitude < eastBorder):
                if identity not in carsInRect:
                    carsInRect.append(identity)
      
    sorted_cars = sorted(carsInRect)
    final_str = ""
    for car in sorted_cars:
        if(final_str == ""):
            final_str += car
        else:
            final_str += "," + car
            
    print(final_str)