with open('input.txt', 'r') as f:
    dat = f.read().strip().split('\n')

data = []
flashedInCycle = []
flashCount = 0

# Read data into array
for r in range(10):
    row = []
    for c in range(10):
        row.append(int(dat[r][c]))
    data.append(row)

def flashOctopuses():
    for r in range(10):
        for c in range(10):
            if data[r][c] == 10 and [r,c] not in flashedInCycle:
                flashOctopus(r,c)

def flashOctopus(x,y):
    global flashCount
    if data[x][y] == 10:
        flashCount+=1
        flashedInCycle.append([x,y])
        increase_adjacent_energy(x,y)

def increase_energy(x,y):
    # Check limits
    if x in [-1, 10,11,12] or y in [-1,10,11,12]:
        return
    else:
        data[x][y] +=1
        if data[x][y] == 10:
            flashOctopus(x,y)
            #increase_adjacent_energy(x,y)


def increase_adjacent_energy(x,y):
    for r in range(x-1,x+2):
        for c in range(y-1,y+2):
            increase_energy(r,c)

def increase_all():
    for r in range(10):
        for c in range(10):
            data[r][c] +=1
            if data[r][c] == 10:
                flashOctopus(r,c)

def printAll():
    for row in range(10):
        print(data[row])

def resetOctopuses():
    for x in range(10):
        for y in range(10):
            if data[x][y] >= 10:
                data[x][y] = 0

def allFlashed():
    allFlashCount = 0
    for r in range(10):
        for c in range(10):
            if data[r][c] == 0:
                allFlashCount+=1
    if allFlashCount == 100:
        return True
    return False

# Part1
for i in range(100):
    flashedInCycle = []
    increase_all()
    flashOctopuses()
    resetOctopuses()
    if allFlashed() == True:
        print("ALL WERE ON FIRST AT " + str(i+1))
        break
print("Part 1 answer = " + str(flashCount))
# Part2
while not allFlashed():
    flashedInCycle = []
    increase_all()
    flashOctopuses()
    resetOctopuses()
    i+=1

print("Part 2 answer = " + str(i+1))

