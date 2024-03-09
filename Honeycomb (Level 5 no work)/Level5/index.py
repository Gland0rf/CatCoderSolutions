import os
import copy

#Pathfinding algorithm initiating (this took far too long) 
def is_exit_point(point, maze):
    i, j = point
    exit = i == 0 or i == len(maze) - 1 or j == 0 or j == len(maze[i]) - 1
    if j == 1 and maze[i][j-1] == "-" or j == len(maze[i]) - 2 and maze[i][j+1] == "-":
        """This is because of a small feature. If we have this line:
            X-X-X-X-X
            -O-W-O-X-
            X-X-X-X-X
            the wasp should still be able to escape, but there is a "-" in the way, which we will have to check for.    
            """
        exit = True
    return exit

def get_neighbors(point, maze):
    
    i, j = point
    neighbors = []
    
    if j >= 2 and maze[i][j - 2] == 'O':
        neighbors.append((i, j - 2))  # One to the left (2 left)
    if j <= len(maze[i]) - 3 and maze[i][j + 2] == 'O':
        neighbors.append((i, j + 2))  # One to the right (2 right)
    if i >= 1 and j >= 1 and maze[i - 1][j - 1] == 'O':
        neighbors.append((i - 1, j - 1))  # One on the top left (1 up and 1 left)
    if i >= 1 and j <= len(maze[i]) - 2 and maze[i - 1][j + 1] == 'O':
        neighbors.append((i - 1, j + 1))  # One on the top right (1 up and 1 right)
    if i <= len(maze) - 2 and j >= 1 and maze[i + 1][j - 1] == 'O':
        neighbors.append((i + 1, j - 1))  # One on the bottom left (1 down and 1 left)
    if i <= len(maze) - 2 and j <= len(maze[i]) - 2 and maze[i + 1][j + 1] == 'O':
        neighbors.append((i + 1, j + 1))  # One on the bottom right (1 down and 1 right)
        
    return neighbors

def mark_visited(point, maze):
    i, j = point
    maze[i][j] = "V"
    
def is_visited(point, maze):
    i, j = point
    maze[i][j] == "V"
    
def dfs(maze, current_point, path_history = []):
    if is_exit_point(current_point, maze):
        return True, path_history + [current_point]
    
    mark_visited(current_point, maze)
    
    neighbors = get_neighbors(current_point, maze)
    for neighbor in neighbors:
        if not is_visited(current_point, maze):
            result, path = dfs(maze, neighbor, path_history + [current_point])
            if result:
                return True, path
            
    return False, path_history

def can_bee_escape(maze, starting_point):
    testing_hive = copy.deepcopy(maze)
    result, path = dfs(testing_hive, starting_point)
    if result:
        return "FREE", path
    else:
        return "TRAPPED", path

def is_bee_trapped(cells, wasp_line, wasp_column):
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
    return bee_state

def get_open_columns(cells, coords):
    line, column = coords
    open_columns = 0
    if(cells[line][column-2] == "O" or cells[line][column-2] == "V"): #Left
        open_columns += 1
    if(cells[line][column+2] == "O" or cells[line][column+2] == "V"): #Right
        open_columns += 1
    if(cells[line-1][column-1] == "O" or cells[line-1][column-1] == "V"): #Top Left
        open_columns += 1
    if(cells[line-1][column+1] == "O" or cells[line-1][column+1] == "V"): #Top Right
        open_columns += 1
    if(cells[line+1][column-1] == "O" or cells[line+1][column-1] == "V"): #Bottom Left
        open_columns += 1
    if(cells[line+1][column+1] == "O" or cells[line+1][column+1] == "V"): #Bottom Right
        open_columns += 1
        
    return open_columns
        
def replaceAroundWasp(cells, waspCoords):
    wasp_line, wasp_column = waspCoords
    if(cells[wasp_line][wasp_column-2] == "O"): #Left
        cells[wasp_line][wasp_column-2] = "X"
    if(cells[wasp_line][wasp_column+2] == "O"): #Right
        cells[wasp_line][wasp_column+2] = "X"
    if(cells[wasp_line-1][wasp_column-1] == "O"): #Top Left
        cells[wasp_line-1][wasp_column-1] = "X"
    if(cells[wasp_line-1][wasp_column+1] == "O"): #Top Right
        cells[wasp_line-1][wasp_column+1] = "X"
    if(cells[wasp_line+1][wasp_column-1] == "O"): #Bottom Left
        cells[wasp_line+1][wasp_column-1] = "X"
    if(cells[wasp_line+1][wasp_column+1] == "O"): #Bottom Right
        cells[wasp_line+1][wasp_column+1] = "X"
        
    return cells

def findAllEscapes(cells, waspCoords):
    can_escape, history = can_bee_escape(cells, waspCoords)
    escapePaths = 0
    while(can_escape == "FREE"):
        escapeSpot = history[-1]
        #print(history)
        if is_exit_point(escapeSpot, cells) and len(history) == 1:
            return escapePaths + 1
        cells[escapeSpot[0]][escapeSpot[1]] = "X"
        can_escape, history = can_bee_escape(cells, waspCoords)
        
        escapePaths += 1
        
    return escapePaths

dir_path = "./input"
files = os.listdir(dir_path)

for file in files:
    inputData = open(dir_path + "/" + file, "r").read()
    
    inputData = inputData.split("\n\n")
    amount_hives = int(inputData[0])
    del inputData[0]
    
    final_str = str(amount_hives) + "\n"
    for x in range(amount_hives):
        hive = inputData[x]
        #Find wasp
        
        lines = hive.split("\n")
        amountBarriers = int(lines[0])
        del lines[0]
        
        wasp_line = -1
        wasp_column = -1
        for x in range(len(lines)):
            line = lines[x]
            wasp_index = line.find("W")
            if(wasp_index != -1):
                wasp_line = x
                wasp_column = wasp_index
        wasp_coords = (wasp_line, wasp_column)
        
        lines = hive.strip().split("\n")
        del lines[0]
        cells = [list(line) for line in lines]
        
        #Option 1: Replace all the spaces around the wasp
        openCellsAroundWasp = get_open_columns(cells, (wasp_line, wasp_column))
        if(openCellsAroundWasp == amountBarriers):
            cells = replaceAroundWasp(cells, (wasp_line, wasp_column))
        else:
            #Option 2:
            for _ in range(amountBarriers):
                sub_hive = copy.deepcopy(cells)
                can_escape, history = can_bee_escape(sub_hive, wasp_coords)
                total_amount_escapes = findAllEscapes(sub_hive, wasp_coords)
                leftToKill = total_amount_escapes
                escape_killers = []
                
                for x, coords in enumerate(history):
                    """if x != 0:
                        
                        if(len(history) <= 2):
                            if(is_exit_point(coords, sub_hive)):
                                sub_hive = copy.deepcopy(cells)
                                sub_hive[coord_before[0]][coord_before[1]] = "X"
                                escapes_found = findAllEscapes(sub_hive, wasp_coords)
                                escape_killers.append([coords, can_escape_sub, escapes_found])
                        else:
                            coord_before = history[x-1]
                            sub_hive = copy.deepcopy(cells)
                            sub_hive[coord_before[0]][coord_before[1]] = "X"
                            result = can_bee_escape(sub_hive, coords)
                            can_escape_sub = True if result[0] == "FREE" else "TRAPPED"
                            escapes_found = ""
                            if(is_exit_point(coords, sub_hive)):
                                escapes_found = findAllEscapes(sub_hive, coord_before)
                                print(escapes_found, coord_before, coords)
                            else:
                                escapes_found = findAllEscapes(sub_hive, coords)
                            escape_killers.append([coords, can_escape_sub, escapes_found])"""
                
                del history[0]
                
                reversed_history = history[::-1]
                for coord in reversed_history:
                    sub_hive = copy.deepcopy(cells)
                    if(reversed_history.index(coord) == len(reversed_history)-1):
                        continue
                    coordAfter = reversed_history[reversed_history.index(coord)+1]
                    print(coord, coordAfter)
                    sub_hive[coordAfter[0]][coordAfter[1]] = "X"
                    escapes_found = findAllEscapes(sub_hive, coordAfter)
                    escape_killers.append([coord, escapes_found])
                
                sorted_escapes = sorted(escape_killers, key=lambda x: x[-1])
                print(sorted_escapes)

                for escape in sorted_escapes:
                    coords = escape[0]
                    escapes_found = escape[1]
                    testing_hive = copy.deepcopy(cells)
                    testing_hive[coords[0]][coords[1]] = "X"
                    paths_found = findAllEscapes(testing_hive, wasp_coords)
                    
                    """if(paths_found == escapes_found):
                        continue
                    if(escapes_found <= total_amount_escapes and escapes_found > 0 or (escapes_found == 1 and leftToKill == 1)):
                        escapes_left = total_amount_escapes - escapes_found
                        leftToKill = escapes_left
                        cells[coords[0]][coords[1]] = "X"
                        break"""
                    
                    if(escapes_found <= paths_found):
                        cells[coords[0]][coords[1]] = "X"
                        break
          
        sub_str = ""  
        for row in cells:
            sub_str += ''.join(row) + "\n"
        
        final_str += "\n" + sub_str
        
    
    file_out = open(f"./output/{file.split(".")[0]}.out", "w")
    file_out.write(final_str)
    file_out.close()