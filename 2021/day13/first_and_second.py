import numpy as np
with open('input.txt','r') as f:
    coordinates, folds = [[i.split(',') for i in item.split('\n')] for item in f.read().split('\n\n')]

# Parse folds
folds = [item[0].replace('fold along ', '').split('=') for item in folds if item[0] != '']
maxX = 0
maxY = 0
for item in coordinates:
    item[0] = int(item[0])
    item[1] = int(item[1])
    if item[0] > maxX: maxX = item[0]
    if item[1] > maxY: maxY = item[1]

# Fill the array
array = np.full((maxY+1, maxX+1), fill_value='.', dtype=str)
for item in coordinates:
    array[item[1]][item[0]] = "#"

def copyArray(arr,xs,xe,ys,ye):
    new_array = np.empty((xe-xs,ye-ys),dtype=str)
    xn = 0
    for x in range(xs,xe):
        yn = 0
        for y in range(ys,ye):
            new_array[xn][yn] = arr[x][y]
            yn+=1
        xn+=1

    return new_array

def combineArraysX(left, right):
    x1,y1 = [item for item in np.shape(left)]
    x2,y2 = [item for item in np.shape(right)]

    for y in range(y2):
        for x in range(x2):
            if right[x][y] == "#":
                left[x][y1-1-y] = "#"
    return left

def combineArraysY(top, bottom):
    x1,y1 = [item for item in np.shape(top)]
    x2,y2 = [item for item in np.shape(bottom)]

    for x in range(x2):
        for y in range(y2):
            if bottom[x][y] == "#":
                top[x1-x-1][y] = "#"
    return top

def foldArray(arr, foldDir, row_col):
    y,x = [item for item in np.shape(arr)]
    row_col_x_2 = row_col 
    row_col_y_2 = row_col 


    if foldDir == 'x':
        row_x_1 = row_col
        row_x_2 = row_col +1

        left_array = copyArray(arr,0,y,0,row_x_1)
        right_array = copyArray(arr,0,y,row_x_2,x)

        return combineArraysX(left_array, right_array)

    elif foldDir == 'y':
        row_y_1 = row_col
        row_y_2 = row_col +1
        
        top_array = copyArray(arr,0,row_y_1,0,x)
        bottom_array = copyArray(arr,row_y_2,y,0,x)

        return combineArraysY(top_array,bottom_array)

def calculateDots(array):
    count = 0
    x_len,y_len= np.shape(array)
    for x in range(x_len):
        for y in range(y_len):
            if array[x][y] == "#":
                count+=1
    return count

def printArray(array):
    count = 0
    x_len,y_len= np.shape(array)
    for x in range(x_len):
        string = []
        for y in range(y_len):
            if array[x][y] == '.':
                string.append(' ')
            else:
                #string.append(array[x][y])
                string.append('█')

        print(string)

# Part1
for idx, item in enumerate(folds):
    array = foldArray(array,str(item[0]),int(item[1]))
    #printArray(array)
    print(f"Dots after fold number {idx+1} = {calculateDots(array)}")

# Part2
printArray(array)


# JGAJEFKU

