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
            expression1 = equasion[0:lastOccurenceOfMinus]
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
    
    #Test 1: Move match between digits
    passed_left = False
    test_equasion_left = leftSide
    for index in find_numbers_indices(leftSide):
        if leftSide[index] in moveable_segments:
            possible_replacements = moveable_segments[leftSide[index]]
            for replacement in possible_replacements:
                test_equasion_left = test_equasion_left[:index] + replacement + test_equasion_left[index+1:]
                if str(evaluate(test_equasion_left)) == rightSide:
                    leftSide = test_equasion_left
                    passed_left = True
                elif str(evaluate(rightSide)) == test_equasion_left:
                    leftSide = test_equasion_left
                    passed_left = True
    
    passed_right = False
    test_equasion_right = rightSide
    if not passed_left:
        for index in find_numbers_indices(rightSide):
            if rightSide[index] in moveable_segments:
                possible_replacements = moveable_segments[rightSide[index]]
                for replacement in possible_replacements:
                    test_equasion_right = test_equasion_right[:index] + replacement + test_equasion_right[index+1:]
                    if str(evaluate(test_equasion_right)) == leftSide:
                        rightSide = test_equasion_right
                        passed_right = True
                    elif str(evaluate(test_equasion_right)) == test_equasion_left:
                        rightSide = test_equasion_right
                        leftSide = test_equasion_left
                        passed_right = True
                    elif str(evaluate(leftSide)) == test_equasion_right:
                        rightSide = test_equasion_right
                        passed_right = True
                    elif str(evaluate(test_equasion_left)) == test_equasion_right:
                        rightSide = test_equasion_right
                        leftSide = test_equasion_left
                        passed_right = True
                        
    if not passed_right:
        #Test 2: Move match between 2 numbers
        passed_left = False
        addable_segments = {"0": ["8"], "1": ["7"], "3": ["9"], "5": ["6", "9"], "6": ["8"], "9": ["8"]}
        removable_segments = {"6": ["5"], "7": ["1"], "8": ["0", "6", "9"], "9": ["3", "5"]}
        for index in find_numbers_indices(leftSide):
            if leftSide[index] in removable_segments:
                possible_replacements = removable_segments[leftSide[index]]
                for replacement in possible_replacements:
                    for sub_index in find_numbers_indices(leftSide):
                        if(sub_index != index):
                            if leftSide[sub_index] in addable_segments:
                                possible_replacements2 = addable_segments[leftSide[sub_index]]
                                for replacement2 in possible_replacements2:
                                    test_equasion = leftSide
                                    test_equasion = test_equasion[:sub_index] + replacement2 + test_equasion[sub_index+1:]
                                    test_equasion = test_equasion[:index] + replacement + test_equasion[index+1:]
                                    if str(evaluate(test_equasion)) == rightSide:
                                        leftSide = test_equasion
                                        passed_left = True
                                    elif str(evaluate(rightSide)) == test_equasion:
                                        leftSide = test_equasion
                                        passed_left = True
        
        if not passed_left:
            addable_segments = {"0": ["8"], "1": ["7"], "3": ["9"], "5": ["6", "9"], "6": ["8"], "9": ["8"]}
            removable_segments = {"6": ["5"], "7": ["1"], "8": ["0", "6", "9"], "9": ["3", "5"]}
            for index in find_numbers_indices(rightSide):
                if rightSide[index] in removable_segments:
                    possible_replacements = removable_segments[rightSide[index]]
                    for replacement in possible_replacements:
                        for sub_index in find_numbers_indices(rightSide):
                            if(sub_index != index):
                                if rightSide[sub_index] in addable_segments:
                                    possible_replacements2 = addable_segments[rightSide[sub_index]]
                                    for replacement2 in possible_replacements2:
                                        test_equasion = rightSide
                                        test_equasion = test_equasion[:sub_index] + replacement2 + test_equasion[sub_index+1:]
                                        test_equasion = test_equasion[:index] + replacement + test_equasion[index+1:]
                                        if str(evaluate(test_equasion)) == leftSide:
                                            rightSide = test_equasion
                                        elif str(evaluate(leftSide)) == test_equasion:
                                            rightSide = test_equasion
                        
    corrected_equasion = f"{leftSide}={rightSide}"
        
    f = open(f"output/{file.split(".")[0]}.out", "w")
    f.write(corrected_equasion)
    f.close()