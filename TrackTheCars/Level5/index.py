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
            
    print(final_str + "\n")