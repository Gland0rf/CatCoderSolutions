import os

dir_path = "./input"
files = os.listdir(dir_path)

for file in files:
    context = open(dir_path + "/" + file, "r").read().split(" ")
    
    amount_to_pay = int(context[0])
    amount_coins = int(context[1])
    del context[0:2]
    
    context = [int(x) for x in context]
    amount_paid = sum(context)
    
    sum_out = abs(amount_to_pay - amount_paid)
    if(amount_paid < amount_to_pay):
        final_str = f"MISSING {sum_out}"
    else:
        final_str = f"CHANGE {sum_out}"
        
    with open(f"output/{file.split(".")[0]}.out", "w") as f:
        f.write(final_str)