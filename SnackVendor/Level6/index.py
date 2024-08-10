import os

dir_path = "./input"
files = os.listdir(dir_path)

def calculate_moves(start, target, prohibited_direction):
    start_row, start_col = start
    target_row, target_col = target
    
    directions = {
        0: (0, 1),
        1: (-1, 1),
        2: (-1, 0),
        3: (-1, -1),
        4: (0, -1),
        5: (1, -1),
        6: (1, 0),
        7: (1, 1)
    }
    
    if prohibited_direction in directions:
        del directions[prohibited_direction]
    
    moves = 0
    current_position = start
    
    while current_position != target:
        current_row, current_col = current_position
        row_diff = target_row - current_row
        col_diff = target_col - current_col
        
        best_move = None
        min_distance = float('inf')
        for direction, (d_row, d_col) in directions.items():
            new_row = current_row + d_row
            new_col = current_col + d_col
            distance = abs(new_row - target_row) + abs(new_col - target_col)
            if distance < min_distance:
                min_distance = distance
                best_move = (d_row, d_col)
                
        current_position = (current_row + best_move[0], current_col + best_move[1])
        moves += 1
    
    return moves
def split_cell(grid_size):
    rows = grid_size[0]
    cols = grid_size[1:]
    return rows, int(cols)

def convert_letter_to_number(letter):
    letter = letter.lower()
    number = ord(letter) - ord('a') + 1
    return number

for file in files:
    context = open(dir_path + "/" + file, "r").read().split(" ")
    
    cell_size = context[0]
    start_pos = context[1]
    target_pos = context[2]
    broken_direction = int(context[3])
    
    start_row, start_col = split_cell(start_pos)
    target_row, target_col = split_cell(target_pos)
    
    start_row = convert_letter_to_number(start_row)
    target_row = convert_letter_to_number(target_row)
    
    total_moves = calculate_moves((start_row, start_col), (target_row, target_col), broken_direction)
        
    with open(f"output/{file.split(".")[0]}.out", "w") as f:
        f.write(str(total_moves))