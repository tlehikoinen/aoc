import numpy as np

# first or second task
first = False

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    data = parseInput(lines)
    listOfCoordinates = []
    for line in data:
        first = Coordinate(line[0], line[1])
        second = Coordinate(line[2], line[3])
        combined = StartToEndCoordinates(first, second)
        listOfCoordinates.append(combined)
    
    # 2D array with size of coordinates max value
    grid = np.zeros((Coordinate.maxSize+1, Coordinate.maxSize), int)
    insertToGrid(grid, listOfCoordinates)
    findOverlaps(grid)

def insertToGrid(grid, startToEndCoordinates):
    for item in startToEndCoordinates:
        if (item.first.x != item.second.x and item.first.y != item.second.y):
            if first == True:
                continue
            drawDiagonally(grid, item)
        else:
            drawLines(grid, item)

def drawDiagonally(grid, coordinates):
    xDif = coordinates.first.x - coordinates.second.x
    yDif = coordinates.first.y - coordinates.second.y
    xValues = np.linspace(coordinates.first.x, coordinates.second.x, num=abs(xDif)+1, dtype=int)
    yValues = np.linspace(coordinates.first.y, coordinates.second.y, num=abs(yDif)+1, dtype=int)
    
    for i in range(abs(xDif)+1):
        grid[yValues[i]][xValues[i]] +=1

def drawLines(grid, coordinates):
    xDif = coordinates.first.x - coordinates.second.x
    yDif = coordinates.first.y - coordinates.second.y
    xValues = np.linspace(coordinates.first.x, coordinates.second.x, num=abs(xDif)+1, dtype=int)
    yValues = np.linspace(coordinates.first.y, coordinates.second.y, num=abs(yDif)+1, dtype=int)
    for y in range(abs(yDif)+1):
        for x in range(abs(xDif)+1):
            grid[yValues[y]][xValues[x]] +=1

def findOverlaps(grid):
    counter = 0
    for x in range(Coordinate.maxSize):
        for y in range(Coordinate.maxSize):
            if grid[x][y] >= 2:
                counter += 1

    print("RESULT")
    print(counter)

def printGrid(grid):
    for i in range(Coordinate.maxSize):
        print(grid[i])

class Coordinate:
    maxSize = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.checkForHighest()
    def checkForHighest(self):
        if self.x > Coordinate.maxSize:
            Coordinate.maxSize = self.x +1
        if self.y > Coordinate.maxSize:
            Coordinate.maxSize = self.y +1

class StartToEndCoordinates:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def printCoordinates(self):
        print("x1 = " + str(self.first.x) + " y1 = " + str(self.first.y))
        print("x2 = " + str(self.second.x) + " y2 = " + str(self.second.y))


def parseInput(inputLines):
    data = []
    for line in inputLines:
        line = line.replace('->', ',')
        line = line.split(',')
        line = [int(i) for i in line]
        data.append(line)
    return data


if __name__ == "__main__":
    main()
