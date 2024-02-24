import os
import math
from shapely.geometry import Point, Polygon

dir_path = "./input"
files = os.listdir(dir_path)

for file in files:
    content = open(dir_path + "/" + file, "r").read().split("\n")
                
    amountSpotted = content[0]
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
                farthestLongitudeTime = time
      
    
    print(farthestLatitudeCar + "," + farthestLatitudeTime + "," + farthestLongitudeCar + "," + farthestLongitudeTime)