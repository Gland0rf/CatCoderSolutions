def findFibo(index):
    
    if(index < 2):
        return index
    
    x = 0
    y = 1
    
    for i in range(index-1):
        tempX = x
        x = y
        y += tempX
    return y

toCalc = [6, 19, 28, 36, 38]

for num in toCalc:
    print(str(findFibo(num)) + "\n")
    
#Leetcode moment