import os

dir_path = "./input"
files = os.listdir(dir_path)

def calculate_coin_change(amount):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    coins_return = []
    
    for coin in coins:
        iterations = 0
        while(amount >= coin):
            amount -= coin
            iterations += 1
        coins_return.append(str(iterations))
        
    return list(reversed(coins_return))

def split_cell(grid_size):
    rows = grid_size[0]
    cols = grid_size[1:]
    return rows, int(cols)

def convert_letter_to_number(letter):
    letter = letter.lower()
    number = ord(letter) - ord('a') + 1
    return number

def convert_number_to_letter(number):
    letter = chr(number + ord('a'))
    return letter

for file in files:
    context = open(dir_path + "/" + file, "r").read().split(" ")
    
    grid_size = context[0]
    del context[0]
    
    rows, cols = split_cell(grid_size)
    rows_num = convert_letter_to_number(rows)
    
    prices = {}
    stock = {}
    
    iteration = 0
    for y in range(rows_num):
        for x in range(cols):
            rows_letter = convert_number_to_letter(y)
            #rows_letter, x+1
            
            prices[f"{rows_letter}{x+1}"] = int(context[iteration])
            iteration += 1
            
    del context[0:iteration]
    
    iteration = 0
    for y in range(rows_num):
        for x in range(cols):
            rows_letter = convert_number_to_letter(y)
            #rows_letter, x+1
            
            stock[f"{rows_letter}{x+1}"] = int(context[iteration])
            iteration += 1
            
    del context[0:iteration]
    
    amount_items_bought = context[0]
    del context[0]
        
    sales = 0
    for slot_bought in context:
        slot_bought = slot_bought.lower()
        if(stock[slot_bought]) == 0:
            continue
        sales += prices[slot_bought]
        stock[slot_bought] -= 1
        
    with open(f"output/{file.split(".")[0]}.out", "w") as f:
        f.write(str(sales))