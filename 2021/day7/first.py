data = open('input.txt').read().strip().split(',')
data = [int(i) for i in data]

fuelCount = 0
position = 0

def calculateFuel(curPosInQuest):
    tempFuelCount = 0
    for d in data:
        tempFuelCount += abs(d-curPosInQuest)

    return tempFuelCount

for i in range(0,max(data)):
    tempFuelCount = calculateFuel(i)
    if fuelCount == 0:
        fuelCount = tempFuelCount
        position = i
    else:
        if tempFuelCount < fuelCount:
            fuelCount = tempFuelCount
            position = i

print(fuelCount)
print(position)

