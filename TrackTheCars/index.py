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
    """firstRectangle = content[0].split(",")
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
                    carsInRect.append(identity)"""
                
    #LEVEL 2
    """amountSpotted = content[0]
    del content[0]
    
    farthestLatitude = -1
    farthestLatitudeCar = ""
    farthestLatitudeTime = ""
    farthestLongitude = -1
    farthestLongitudeCar = ""
    farthestLongitudeTime = ""
    
    for carSpotted in content:
        if(carSpotted != ""):
            carSpotted = carSpotted.split(",")
            identity = carSpotted[0]
            time = carSpotted[1]
            latitude = float(carSpotted[2])
            longitude = float(carSpotted[3])
            
            if(latitude > farthestLatitude or farthestLatitude == -1):
                farthestLatitude = latitude
                farthestLatitudeCar = identity
                farthestLatitudeTime = time
            if(longitude > farthestLongitude or farthestLongitude == -1):
                farthestLongitude = longitude
                farthestLongitudeCar = identity
                farthestLongitudeTime = time"""
      
    #LEVEL 3 
    """sorted_cars = sorted(carsInRect)
    final_str = ""
    for car in sorted_cars:
        if(final_str == ""):
            final_str += car
        else:
            final_str += "," + car"""
            
            
            
    #LEVEL 4
    amount_points_start_polygon = int(content[0])
    pointsStartPolygon = []
    
    cars_positions_found = []
    cars_found = []
    
    del content[0]
    for x in range(0, amount_points_start_polygon):
        point = content[x]
        point = point.split(",")
        latitude = float(point[0])
        longitude = float(point[1])
        coordinates = (latitude, longitude)
        pointsStartPolygon.append(coordinates)
        
    amount_points_end_polygon = int(content[amount_points_start_polygon])
    pointsEndPolygon = []
    
    del content[0]
    for x in range(amount_points_start_polygon, amount_points_start_polygon + amount_points_end_polygon):
        point = content[x]
        point = point.split(",")
        latitude = float(point[0])
        longitude = float(point[1])
        coordinates = (latitude, longitude)
        pointsEndPolygon.append(coordinates)
    
    start_index = amount_points_end_polygon+amount_points_start_polygon
    amount_positions = int(content[start_index])
    for x in range(start_index+1, start_index+amount_positions+1):
        position = content[x]
        position = position.split(",")
        identity = position[0]
        time = position[1]
        latitude = float(position[2])
        longitude = float(position[3])
        carCoordinates = (latitude, longitude)
        
        time = time.split(":")
        hours = int(time[0])
        minutes = int(time[1])
        seconds = int(time[2])
        
        if(is_time_in_range(hours, minutes, seconds, (9, 30, 0), (10, 45, 0))):
            is_point_in_first_polygon = is_inside_polygon(carCoordinates, pointsStartPolygon)
            if is_point_in_first_polygon and identity not in cars_found and identity not in cars_positions_found:
                cars_positions_found.append(identity)
            else:
                is_point_in_second_polygon = is_inside_polygon(carCoordinates, pointsEndPolygon)
                if(is_point_in_second_polygon):
                    if(identity in cars_positions_found and identity not in cars_found):
                        cars_found.append(identity)
    
    sorted_cars = sorted(cars_found)
    final_str = ""
    for car in sorted_cars:
        if(final_str == ""):
            final_str += car
        else:
            final_str += "," + car
            
    print(final_str + "\n\n\n")
    #print(is_inside_polygon((48.6333,15.8531), [(48.6334,15.8532), (48.6334,14.2856), (48.3023,14.2856), (48.3023, 15.8532)]))