from shapely.geometry import Polygon, Point
import pandas as pd
from datetime import datetime

# Function to check if a point is inside a polygon
def is_point_inside_polygon(point, polygon):
    return polygon.contains(point)

# Eingabedaten
input_lines = [
    "4",
    "48.2334,15.4532",
    "48.2334,14.9856",
    "48.1023,14.9856",
    "48.1023, 15.4532",
    "4",
    "48.6334,15.8532",
    "48.6334,14.2856",
    "48.3023,14.2856",
    "48.3023, 15.8532",
    "260",
    "G-4398,09:00:30,48.2289,14.5287",
    "Z-3595,09:00:30,47.0236,13.6089",
    "O-3872,09:00:30,47.0139,13.1829",
    "Y-2671,09:00:30,47.6607,13.609",
    "V-5959,09:00:30,48.1501,15.4203",
    "S-2417,09:00:30,48.7384,15.1149"
]

# Extract polygons
n = int(input_lines[0])
polygon1_coords = [tuple(map(float, point.split(','))) for point in input_lines[1:1 + n]]
polygon1 = Polygon(polygon1_coords)

m = int(input_lines[1 + n])
polygon2_coords = [tuple(map(float, point.split(','))) for point in input_lines[2 + n:2 + n + m]]
polygon2 = Polygon(polygon2_coords)

# Extract observations
k = int(input_lines[2 + n + m])
observations = [line.split(',') for line in input_lines[3 + n + m:]]
df = pd.DataFrame(observations, columns=['Kennz', 'Zeit', 'Laengengr', 'Breitengr'])
df['Zeit'] = pd.to_datetime(df['Zeit'], format='%Y-%m-%d %H:%M:%S')

# Filter observations between 9:30 and 10:45
start_time = datetime.strptime('9:30:00', '%H:%M:%S')
end_time = datetime.strptime('10:45:00', '%H:%M:%S')
filtered_df = df[(df['Zeit'] >= start_time) & (df['Zeit'] <= end_time)]

# Identify vehicles that moved between the two polygons
moving_vehicles = []
for index, row in filtered_df.iterrows():
    point = Point(float(row['Laengengr']), float(row['Breitengr']))
    if is_point_inside_polygon(point, polygon1) and is_point_inside_polygon(point, polygon2):
        moving_vehicles.append(row['Kennz'])

# Output the identified vehicles
print("Vehicles that moved between 9:30 and 10:45 from one polygon to another:")
print(moving_vehicles)