import os

dir_path = "./input"
files = os.listdir(dir_path)

def get_first_open_spot(parkings_taken):
    for key in parkings_taken:
        if parkings_taken[key] == 0:
            return key
    return None

def get_key_by_value(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return None

def get_price_for_weight(set_price, weight):
    extra_price = 0
    while weight > 0:
        extra_price += set_price
        weight -= 100
        
    return extra_price
        

for f, file in enumerate(files):
    inputData = open(dir_path + "/" + file, "r").read().split("\n")
    
    parking_plots = int(inputData[0].split(" ")[0])
    car_amount = int(inputData[0].split(" ")[1])
    
    price_amount = inputData[1].split(" ")
    price_amount = [int(x) for x in price_amount]
    
    weight_data = inputData[2].split(" ")
    car_weights = {}
    for car_index, weight in enumerate(weight_data):
        car_weights[car_index+1] = int(weight)
    
    car_data = inputData[3].split(" ")
    
    queue = []
    parkings_taken = {}
    revenue = 0
    
    for i in range(parking_plots):
        parkings_taken[i] = 0
    
    for car in car_data:
        car = int(car)
        if car > 0:
            open_spot = get_first_open_spot(parkings_taken)
            if open_spot != None:
                parkings_taken[open_spot] = car
            else:
                queue.append(car)
        else:
            spot = get_key_by_value(parkings_taken, abs(car))
            parkings_taken[spot] = 0
            
            start_price = price_amount[spot]
            revenue += get_price_for_weight(start_price, car_weights[abs(car)])
            
            if(len(queue) > 0):
                open_spot = get_first_open_spot(parkings_taken)
                parkings_taken[open_spot] = queue[0]
                queue.pop(0)
    
    file_out = open(f"./output/output_{f}.out", "w")
    file_out.write(str(revenue))
    file_out.close()