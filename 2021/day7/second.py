data = open('input.txt').read().strip().split(',')
data = [int(i) for i in data]

fuelCount = 0
position = 0
maxNumber = max(data)

# Second task helper list, where each index has sums of previous indexes added
fuelBurnRates = []
tempBurn = 0
for i in range(maxNumber+1):
    tempBurn += i
    fuelBurnRates.append(tempBurn)

def calculateFuel(curPosInQuest):
    tempFuelCount = 0
    for d in data:
        tempFuelCount += fuelBurnRates[abs(d-curPosInQuest)]

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

