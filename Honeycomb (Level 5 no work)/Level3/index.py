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
        
        bee_free = False
        bee_blocked = False
        #Right
        for i in range(0, len(cells[wasp_line])-wasp_column, 2):
            current_column = wasp_column + i
            if(cells[wasp_line][current_column] == "X"):
                bee_blocked = True
        if not bee_blocked:
            bee_free = True
        bee_blocked = False
        #Left
        if not bee_free:
            for i in range(wasp_column, -1, -2):
                if(cells[wasp_line][i] == "X"):
                    bee_blocked = True
        if not bee_blocked:
            bee_free = True
        bee_blocked = False
        #Top Left
        if not bee_free:
            for i in range(0, wasp_line+1, 1):
                y = wasp_line - i
                x = wasp_column - i
                if x >= len(cells[y]) or x < 0:
                    break
                if(cells[y][x] == "X"):
                    bee_blocked = True
        if not bee_blocked:
            bee_free = True
        bee_blocked = False
        #Top Right
        if not bee_free:
            for i in range(0, wasp_line+1, 1):
                y = wasp_line - i
                x = wasp_column + i
                if x >= len(cells[y]) or x < 0:
                    break
                if(cells[y][x] == "X"):
                    bee_blocked = True
        if not bee_blocked:
            bee_free = True
        bee_blocked = False
        #Bottom Left
        if not bee_free:
            for i in range(0, len(cells)-wasp_line, 1):
                y = wasp_line + i
                x = wasp_column - i
                if x >= len(cells[y]) or x < 0:
                    break
                if(cells[y][x] == "X"):
                    bee_blocked = True
        if not bee_blocked:
            bee_free = True
        bee_blocked = False
        #Bottom Right
        if not bee_free:
            for i in range(0, len(cells)-wasp_line, 1):
                y = wasp_line + i
                x = wasp_column + i
                if x >= len(cells[y]) or x < 0:
                    break
                if(cells[y][x] == "X"):
                    bee_blocked = True
        if not bee_blocked:
            bee_free = True
        bee_blocked = False
                
        bee_state = "FREE"
        if not bee_free:
            bee_state = "TRAPPED"
        final_str += bee_state + "\n"
    
    file_out = open(f"./output/{file.split(".")[0]}.out", "w")
    file_out.write(final_str)
    file_out.close()