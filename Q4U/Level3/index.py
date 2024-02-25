import os

dir_path = "./input"
files = os.listdir(dir_path)

def max_subarray_sum(arr):
    current_sum = 0
    result = arr[0]
    start_index = 0
    end_index = 0
    current_start = 1
    result_indexes = [(0, 0)]

    for i in range(1, len(arr)):
        num = arr[i]
        if current_sum < 0:
            current_sum = num
            current_start = i
        else:
            current_sum += num

        if current_sum > result:
            result = current_sum
            start_index = current_start
            end_index = i
            result_indexes = [(start_index+1, end_index+1)]
        elif current_sum == result:
            result_indexes.append((current_start+1, i+1))

    return result, result_indexes

for file in files:
    content = open(dir_path + "/" + file, "r").read().split(" ")
    
    queue = int(content[0])
    del content[0]
    
    #Convert array to ints
    content = [int(x) for x in content]
    
    best_start_capital, indexes = max_subarray_sum(content)
    possibilities = len(indexes)
    
    final_str = f"{best_start_capital} {possibilities}"
    for start, end in indexes:
        final_str += f" {start} {end}"
        
    print(final_str)