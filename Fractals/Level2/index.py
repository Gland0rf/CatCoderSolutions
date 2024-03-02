import os
import math

dir_path = "./input"
files = os.listdir(dir_path)

for file in files:
    inputData = open(dir_path + "/" + file, "r").read().split(" ")
    
    shape_type = inputData[0]
    length = int(inputData[1].split("=")[1])
    iterations = int(inputData[2].split("=")[1])
    
    perimiter = 0
    if(shape_type == "tri"):
        #Pn = P1*(4/3)^n-1
        p0 = 3 * length
        perimiter = p0 * math.pow(4, iterations) / math.pow(3, iterations)
    elif(shape_type == "sq"):
        #Pn = P1*(5/3)^n-1
        p0 = 4 * length
        perimiter = p0 * math.pow(5, iterations) / math.pow(3, iterations)
            
    print(int(perimiter))