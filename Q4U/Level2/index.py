import os

dir_path = "./input"
files = os.listdir(dir_path)

def max_subarray_sum(arr):
    current_sum = 0
    result = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]
        if current_sum < 0:
            current_sum = num
        else:
            current_sum += num

        if current_sum > result:
            result = current_sum

    return result

for file in files:
    content = open(dir_path + "/" + file, "r").read().split(" ")
    
    queue = int(content[0])
    del content[0:1]
    
    #Convert array to ints
    content = [int(x) for x in content]
    
    best_start_capital = max_subarray_sum(content)
    
    print(best_start_capital)