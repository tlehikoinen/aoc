import numpy as np
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
            if data[x-1][y] > num and data [x][y+1] > num:
                lowPoints.append([x,y])
        elif y == colLength-1:
            if data[x-1][y] > num and data[x][y-1] > num:
                lowPoints.append([x,y])
            pass
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

for x in range(len(data)):
    for y in range(len(data[x])):
        findLowPoints(x,y, data[x][y])

lowPointValues = []
for item in lowPoints:
    lowPointValues.append(data[item[0]][item[1]])

#print(riskLevels)
print("Sum of risk levels")
print(np.sum([int(i)+1 for i in lowPointValues]))

