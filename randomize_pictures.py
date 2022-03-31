import random

def randomize_pictures(path):
    output="test,image\n"
    lineList = []
    with open(path) as f:
        for line in f:
            if line == "test,image\n":
                continue
            lineList.append(line)
    random.shuffle(lineList)
    for line in lineList:
        output += line
    f= open(path,"w")
    f.write(output)
        

randomize_pictures('output/scaledImages.csv')