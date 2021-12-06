import sys
import numpy as np
try:
    if sys.argv[1] == '-t':
        inputfile = 'testinput.txt'
    else:
        inputfile = 'input.txt'
except:
    inputfile = 'input.txt'

with open(inputfile, 'r') as f:
    line = f.readline()

data = [int(i) for i in line.split(',')]
days = 256

# Array indexes are lantern counters
# value of the index is the count of lanternfishes with that timer count
lanterns = np.zeros(9, dtype='int64')

# Initial state
for row in data:
    lanterns[row] +=1

# Initial fish count
fishCounter = len(data)

for day in range(days):
    # Save first item and move others to position -1
    zeroCount = lanterns[0]
    for index in range(len(lanterns)-1):
       lanterns[index] = lanterns[index+1]

    fishCounter += zeroCount
    lanterns[8] = zeroCount
    lanterns[6] += zeroCount
 
print("RESULT =\n" + str(fishCounter))
