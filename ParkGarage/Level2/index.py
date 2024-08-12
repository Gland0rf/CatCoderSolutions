import os

dir_path = "./input"
files = os.listdir(dir_path)

def get_max_cars(car_data):
    current_cars = 0
    max_cars = 0
    for car in car_data:
        if int(car) > 0:
            current_cars += 1
            if current_cars > max_cars:
                max_cars =current_cars
        else:
            current_cars -= 1
    
    return max_cars

def get_max_waiting(car_data, parking_plots):
    current_cars = 0
    
    waiting_list = 0
    max_waiting_list = 0
    
    for car in car_data:
        if int(car) > 0:
            current_cars += 1
            if current_cars > parking_plots:
                waiting_list += 1
                if waiting_list > max_waiting_list:
                    max_waiting_list = waiting_list
        else:
            if current_cars > parking_plots:
                waiting_list -= 1
            current_cars -= 1
    
    return max_waiting_list

for f, file in enumerate(files):
    inputData = open(dir_path + "/" + file, "r").read().split("\n")
    
    parking_plots = int(inputData[0].split(" ")[0])
    car_amount = int(inputData[0].split(" ")[1])
    
    car_data = inputData[1].split(" ")
    
    max_cars = get_max_cars(car_data)
    max_waiting_list = get_max_waiting(car_data, parking_plots)
    
    if max_cars > parking_plots: max_cars = parking_plots
    
    final_str = f"{max_cars} {max_waiting_list}"
    
    file_out = open(f"./output/output_{f}.out", "w")
    file_out.write(final_str)
    file_out.close()