# Read lines from the file and store them into variable
with open('input.txt', 'r') as f:
    lines = f.readlines()

# Helper array for storing values
array = [0] * 12
arrayFlipped = [0] * 12
# Increment indexes of helper array with 1 or 0
for line in lines:
    for index, item in enumerate(line):
        if item == '1':
            array[index] += 1

# Convert helper array to 1 and 0 depending which one was more common
for index, item in enumerate(array):
    if item > len(lines)/2:
        array[index] = 1
        arrayFlipped[index] = 0
    else:
        array[index] = 0
        arrayFlipped[index] = 1


def convertToDecimal(array):
    decimal = 0
    powerOf = len(array)-1
    for i in range(len(array)):
        decimal += (2**powerOf)*array[i]
        powerOf-=1
    return decimal
        
decArray = convertToDecimal(array)
decArrayFlipped = convertToDecimal(arrayFlipped)

print(decArray * decArrayFlipped)

