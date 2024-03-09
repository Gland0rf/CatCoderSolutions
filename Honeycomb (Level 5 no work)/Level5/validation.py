import os

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
    
def dfs(maze, current_point):
    if is_exit_point(current_point, maze):
        return True
    
    mark_visited(current_point, maze)
    
    neighbors = get_neighbors(current_point, maze)
    for neighbor in neighbors:
        if not is_visited(current_point, maze):
            if dfs(maze, neighbor):
                return True
            
    return False

def can_bee_escape(maze, starting_point):
    if dfs(maze, starting_point):
        return "FREE"
    else:
        return "TRAPPED"


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

dir_path = "./output"
files = os.listdir(dir_path)

for file in files:
    #Skip validation files
    if(file.startswith("validation")):
        continue
    inputData = open(dir_path + "/" + file, "r").read()
    
    inputData = inputData.split("\n\n")
    amount_hives = int(inputData[0])
    del inputData[0]
    
    final_str = ""
    for x in range(amount_hives):
        hive = inputData[x]
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
        wasp_coords = (wasp_line, wasp_column)
              
        
        lines = hive.strip().split("\n")
        cells = [list(line) for line in lines]
                    
        result = can_bee_escape(cells, wasp_coords)
        
        final_str += result + "\n"
    
    file_out = open(f"./output/validation-{file.split(".")[0]}.out", "w")
    file_out.write(final_str)
    file_out.close()