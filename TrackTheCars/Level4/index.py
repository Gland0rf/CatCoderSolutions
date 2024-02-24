import os
import math
from shapely.geometry import Point, Polygon
#Make sure to import! "pip install shapely"

dir_path = "./input"
files = os.listdir(dir_path)

def is_inside_polygon(point, polygon_coords):
    point = Point(point)
    
    polygon = Polygon(polygon_coords)
    
    return polygon.contains(point)

    

for file in files:
    content = open(dir_path + "/" + file, "r").read().split("\n")
           
    cars_found = 0 
    
    amount_points_polygon = int(content[0])
    pointsPolygon = []
    
    del content[0]
    for x in range(0, amount_points_polygon):
        point = content[x]
        point = point.split(",")
        latitude = float(point[0])
        longitude = float(point[1])
        coordinates = (latitude, longitude)
        pointsPolygon.append(coordinates)  
    
    start_index = amount_points_polygon
    amount_positions = int(content[start_index])
    
    for x in range(start_index+1, start_index+amount_positions+1):
        position = content[x]
        position = position.split(",")
        latitude = float(position[0])
        longitude = float(position[1])
        carCoordinates = (latitude, longitude)
        is_car_inside_polygon = is_inside_polygon(carCoordinates, pointsPolygon)
        if(is_car_inside_polygon):
            cars_found += 1
        
    
    print(cars_found)