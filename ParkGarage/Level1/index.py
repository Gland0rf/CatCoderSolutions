import os

dir_path = "./input"
files = os.listdir(dir_path)

for f, file in enumerate(files):
    inputData = open(dir_path + "/" + file, "r").read().split("\n")
    
    parking_plots = int(inputData[0].split(" ")[0])
    parking_plots = int(inputData[0].split(" ")[1])
    
    car_data = inputData[1].split(" ")
    
    current_cars = 0
    max_cars = 0
    for car in car_data:
        if int(car) > 0:
            current_cars += 1
            if current_cars > max_cars:
                max_cars =current_cars
        else:
            current_cars -= 1
    
    file_out = open(f"./output/output_{f}.out", "w")
    file_out.write(str(max_cars))
    file_out.close()