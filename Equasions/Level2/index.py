import os
import re

dir_path = "./input"
files = os.listdir(dir_path)

def evaluate(equasion):
    if equasion.isdigit():
        return int(equasion)
    elif(equasion[0] == "-"):
        return -evaluate(equasion[1:len(equasion)])
    else:
        lastOccurenceOfPlus = equasion.rfind("+")
        lastOccurenceOfMinus = equasion.rfind("-")
        if(lastOccurenceOfPlus != -1):
            expression1 = equasion[0:lastOccurenceOfPlus]
            expression2 = equasion[lastOccurenceOfPlus+1:len(equasion)]
            return evaluate(expression1) + evaluate(expression2)
        elif(lastOccurenceOfMinus != -1):
            expression1 = equasion[0:lastOccurenceOfMinus-1]
            expression2 = equasion[lastOccurenceOfMinus+1:len(equasion)]
            return evaluate(expression1) - evaluate(expression2)
        
        
def find_numbers_indices(input_string):
    pattern = r'\d+'
    matches = re.finditer(pattern, input_string)
    
    indices = [match.start() for match in matches]

    return indices

moveable_segments = {"0": ["6", "9"], "2": ["3"], "3": ["2", "5"], "5": ["3"], "6": ["0", "9"], "9": ["0", "6"]}

for file in files:
    equasion = open(dir_path + "/" + file, "r").read()
    
    corrected_equasion = ""
    
    equasion = equasion.split("=")
    leftSide = equasion[0]
    rightSide = equasion[1]
    
    passed_left = False
    for index in find_numbers_indices(leftSide):
        if leftSide[index] in moveable_segments:
            possible_replacements = moveable_segments[leftSide[index]]
            for replacement in possible_replacements:
                test_equasion = leftSide
                test_equasion = test_equasion[:index] + replacement + test_equasion[index+1:]
                if str(evaluate(test_equasion)) == rightSide:
                    leftSide = test_equasion
                    passed_left = True
                elif str(evaluate(rightSide)) == test_equasion:
                    leftSide = test_equasion
                    passed_left = True
      
    if not passed_left:
        for index in find_numbers_indices(rightSide):
            if rightSide[index] in moveable_segments:
                possible_replacements = moveable_segments[rightSide[index]]
                for replacement in possible_replacements:
                    test_equasion = rightSide
                    test_equasion = test_equasion[:index] + replacement + test_equasion[index+1:]
                    print(test_equasion, equasion, str(evaluate(test_equasion)))
                    if str(evaluate(test_equasion)) == leftSide:
                        rightSide = test_equasion
                    elif str(evaluate(leftSide)) == test_equasion:
                        rightSide = test_equasion
                        
    corrected_equasion = f"{leftSide}={rightSide}"
        
    f = open(f"output/{file.split(".")[0]}.out", "w")
    f.write(corrected_equasion)
    f.close()