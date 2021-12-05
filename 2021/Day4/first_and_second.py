def main():
    with open('input.txt', 'r') as f:
        bingoInput = f.readlines()

    bingoNumbers = parseBingoNumbers(bingoInput[0])
    bingoGrids = parseInputIntoBingoGrids(bingoInput)

    bingoGridsWithBingo = []
    for number in bingoNumbers:
        BingoGrid.lastInserted = number
        for grid in bingoGrids:
            grid.newBingoNumber(number)
            if grid.checkForBingo() == True:
                # Print result for the first match
                if len(bingoGridsWithBingo) == 0:
                    print("FIRST TO WIN")
                    grid.printResult()

                if grid.identifier not in bingoGridsWithBingo:
                    bingoGridsWithBingo.append(grid.identifier)
 
                # Print result for the last match
                if len(bingoGridsWithBingo) == len(bingoGrids):
                    print("LAST TO WIN")
                    grid.printResult()
                    return

def parseInputIntoBingoGrids(bingoInput):
    bingoGrids = []
    for index, i in enumerate(range(2, len(bingoInput), 6)):
        grid = BingoGrid(index)
        for y in range(5):
            bingoRow = parseRow(bingoInput[i+y])
            bingoRow = [BingoNumber(i) for i in bingoRow]
            grid.bingoGrid.insert(y, bingoRow)
        bingoGrids.insert(index, grid)

    return bingoGrids

def parseBingoNumbers(bingoNumberInput):
    bingoNumbers = []
    bingoNumbers = bingoNumberInput.split(',')
    bingoNumbers = [int(i) for i in bingoNumbers]
    return bingoNumbers

# Remove empty items
def parseRow(row):
    row = row.split(' ')
    newRow = []
    for item in row:
        if item == "":
            continue
        else:
            newRow.append(item)
    newRow = [int(i) for i in newRow]
    return newRow

class BingoNumber:
    def __init__(self, number):
        self.number = number
        self.chosen = False

    def setChosen(self):
        self.chosen = True
        
class BingoGrid:
    lastInserted = 0
    def __init__(self, identifier):
        self.identifier = identifier
        self.bingoGrid = []

    def newBingoNumber(self, number):
        for x in range(5):
            for y in range(5):
                if self.bingoGrid[x][y].number == number:
                    self.bingoGrid[x][y].chosen = True

    def printResult(self):
        sumCounter = 0
        for x in range(5):
            for y in range(5):
                if self.bingoGrid[x][y].chosen == False:
                    sumCounter += self.bingoGrid[x][y].number
        print(sumCounter*BingoGrid.lastInserted)

    def checkForVerticalBingo(self):
        bingo = False
        verticalCounter = 0
        for x in range(5):
            for y in range(5):
                if self.bingoGrid[x][y].chosen == True:
                    verticalCounter += 1
            if verticalCounter == 5:
                return True
            else:
                verticalCounter = 0
        return False


    def checkForHorizontalBingo(self):
        bingo = False
        horizontalCounter = 0
        for y in range(5):
            for x in range(5):
                if self.bingoGrid[x][y].chosen == True:
                    horizontalCounter += 1
            if horizontalCounter == 5:
                return True
            else:
                horizontalCounter = 0
        return False

    def checkForBingo(self):
        if (self.checkForVerticalBingo() or self.checkForHorizontalBingo()):
            return True
        else:
            return False

if __name__ == "__main__":
    main()
