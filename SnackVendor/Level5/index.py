import os

dir_path = "./input"
files = os.listdir(dir_path)

def calculate_moves(start, target):
    start_row, start_col = start
    target_row, target_col = target
    
    row_difference = abs(start_row - target_row)
    col_difference = abs(start_col - target_col)
    
    total_moves = max(row_difference, col_difference)
    return total_moves

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
    
    start_row, start_col = split_cell(start_pos)
    target_row, target_col = split_cell(target_pos)
    
    start_row = convert_letter_to_number(start_row)
    target_row = convert_letter_to_number(target_row)
    
    total_moves = calculate_moves((start_row, start_col), (target_row, target_col))
    print(total_moves)
        
    with open(f"output/{file.split(".")[0]}.out", "w") as f:
        f.write(str(total_moves))