import os

dir_path = "./input"
files = os.listdir(dir_path)

for file in files:
    inputData = open(dir_path + "/" + file, "r").read()
    
    inputData = inputData.split("\n\n")
    amount_hives = int(inputData[0])
    del inputData[0]
    
    final_str = ""
    for hive in inputData:
        #Find wasp
        
        lines = hive.split("\n")
        
        wasp_line = -1
        wasp_column = -1
        for x in range(len(lines)):
            line = lines[x]
            wasp_index = line.find("W")
            if(wasp_index != -1):
                wasp_line = x
                wasp_column = wasp_index
              
        
        lines = hive.strip().split("\n")
        cells = [list(line) for line in lines]
        
        open_columns = 0
        if(cells[wasp_line][wasp_column-2] == "O"): #Left
            open_columns += 1
        if(cells[wasp_line][wasp_column+2] == "O"): #Right
            open_columns += 1
        if(cells[wasp_line-1][wasp_column-1] == "O"): #Top Left
            open_columns += 1
        if(cells[wasp_line-1][wasp_column+1] == "O"): #Top Right
            open_columns += 1
        if(cells[wasp_line+1][wasp_column-1] == "O"): #Bottom Left
            open_columns += 1
        if(cells[wasp_line+1][wasp_column+1] == "O"): #Bottom Right
            open_columns += 1
    
        final_str += str(open_columns) + "\n"
    
    file_out = open(f"./output/{file.split(".")[0]}.out", "w")
    file_out.write(final_str)
    file_out.close()