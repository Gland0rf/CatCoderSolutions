import os

dir_path = "./input"
files = os.listdir(dir_path)

for file in files:
    inputData = open(dir_path + "/" + file, "r").read()
    
    inputData = inputData.split("\n")
    cell_count = 0
    for line in inputData:
        cell_count += line.count("O")
        
    print(cell_count)
    file_out = open(f"./output/{file.split(".")[0]}.out", "w")
    file_out.write(str(cell_count))
    file_out.close()