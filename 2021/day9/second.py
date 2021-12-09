import numpy as np
import time
start_time = time.time()
with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

colLength = len(data[0])
rowLength = len(data)
print(rowLength)
print(colLength)
lowPoints = []

def findLowPoints(x,y, num):
    global lowPoints
    # Top row
    if x == 0:
        if y == 0:
            if data[x+1][y] > num and data[x][y+1] > num:
                lowPoints.append([x,y])
        elif y == colLength-1:
            if data[x][y-1] > num and data[x+1][y] > num:
                lowPoints.append([x,y])
        else:
            if data[x+1][y] > num and data[x][y-1] > num and data[x][y+1] > num:
                lowPoints.append([x,y])
    # Bottom row
    elif x == rowLength-1:
        if y == 0:
            if data[x-1][y] > num and data[x][y+1] > num:
                lowPoints.append([x,y])
        elif y == colLength-1:
            if data[x-1][y] > num and data[x][y-1] > num:
                lowPoints.append([x,y])
        else:
            if data[x-1][y] > num and data[x][y-1] > num and data[x][y+1] > num:
                lowPoints.append([x,y])
    # Middle rows
    else:
        if y == 0:
            if data[x-1][y] > num and data[x+1][y] > num and data[x][y+1]>num:
                lowPoints.append([x,y])

        elif y == colLength-1:
            if data[x-1][y] > num and data[x+1][y] > num and data[x][y-1]>num:
                lowPoints.append([x,y])

        else:
            if data[x-1][y] > num and data[x+1][y] > num and data[x][y-1] > num and data[x][y+1] > num:
                lowPoints.append([x,y])

basinCounter = 0
alreadyVisited = []
# Finding all basins recursively
def findBasins(prevX,prevY,curX,curY):
    global basinCounter
    global alreadyVisited
    directions = {"left":[0,-1],"right":[0,1],"up":[-1,0],"down":[1,0]}
    iteration = 0

    # Return if pos is over limits or equals 9
    if curX == -1 or curX == rowLength or curY == -1 or curY == colLength:
        return
    if int(data[curX][curY]) == 9:
        return
    # Return if pos already belongs to basin
    if [curX,curY] in alreadyVisited:
        return

    # Return if current value isn't bigger by one than previous
    # Doesn't check if prev and cur values equal (start condition)
    if prevX != curX and prevY != curY:
        if int(data[prevX][prevY])-int(data[curX][curY]) != 1:
            return

    alreadyVisited.append([curX,curY])
    basinCounter+=1
    
    # Iterate over every direction
    for key, value in directions.items():
        findBasins(curX,curY,curX+value[0],curY+value[1])


# Programs
#
# Part1
for x in range(len(data)):
    for y in range(len(data[x])):
        findLowPoints(x,y, data[x][y])

lowPointValues = []
for item in lowPoints:
    lowPointValues.append(data[item[0]][item[1]])

#print(riskLevels)
print("Sum of risk levels")
print(np.sum([int(i)+1 for i in lowPointValues]))
print("--- %s seconds ---" % (time.time() - start_time))

# Part2
basins = []
for item in lowPoints:
    basinCounter = 0
    findBasins(int(item[0]), int(item[1]),int(item[0]), int(item[1]))
    basins.append(basinCounter)

basins.sort(reverse = True)
print(basins)
print(basins[0]*basins[1]*basins[2])



