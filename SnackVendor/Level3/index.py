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
    
    iteration = 0
    for y in range(rows_num):
        for x in range(cols):
            rows_letter = convert_number_to_letter(y)
            #rows_letter, x+1
            
            prices[f"{rows_letter}{x+1}"] = context[iteration]
            iteration += 1
            
    del context[0:iteration]
    
    slot_bought = context[0]
    amount_coins_inserted = int(context[1])
    del context[0:2]
    
    amount_to_pay = int(prices[slot_bought.lower()])
    
    context = [int(x) for x in context]
    amount_paid = sum(context)
    
    sum_out = abs(amount_to_pay - amount_paid)
    if(amount_paid < amount_to_pay):
        final_str = f"MISSING {sum_out}"
    else:
        return_money = calculate_coin_change(sum_out)
        final_str = f"CHANGE {' '.join(return_money)}"
        
    with open(f"output/{file.split(".")[0]}.out", "w") as f:
        f.write(final_str)