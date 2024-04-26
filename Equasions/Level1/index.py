import os

dir_path = "./input"
files = os.listdir(dir_path)

moveable_segments = {"0": ["6", "9"], "2": ["3"], "3": ["2", "5"], "5": ["3"], "6": ["0", "9"], "9": ["0", "6"]}

for file in files:
    equasion = open(dir_path + "/" + file, "r").read()
    
    equasion = equasion.split("=")
    leftSide = equasion[0]
    rightSide = equasion[1]
    
    corrected_equasion = ""
    
    if leftSide in moveable_segments:
        possible_replacements = moveable_segments[leftSide]
        
        for replacement in possible_replacements:
            print(replacement, leftSide)
            if replacement == rightSide:
                corrected_equasion = f"{replacement}={rightSide}"
                break
    elif rightSide in moveable_segments:
        possible_replacements = moveable_segments[rightSide]
        
        for replacement in possible_replacements:
            if replacement == leftSide:
                corrected_equasion = f"{replacement}={rightSide}"
                break
    else:
        corrected_equasion = "Not possible"
        
    f = open(f"output/{file.split(".")[0]}.out", "w")
    f.write(corrected_equasion)
    f.close()