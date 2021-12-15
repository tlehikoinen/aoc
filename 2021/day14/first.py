import collections
import numpy as np
from numpy import uint64
with open('input.txt','r') as f:
    data = f.read().strip().split('\n')


# Inefficient but gets the result for Part1

polymer = data[0]
insertion_rules =[[i[0],i[1]] for i in [item.split(' -> ') for item in data[2:]]]

# Dict for letters, stores every index the letter appears in its value as list
# Initiliase list
letters = collections.defaultdict(list)

valueCount = 0
for idx in range(len(polymer)):
    #letters.setdefault(polymer[idx],[]).append(idx)
    letters[polymer[idx]].append(idx)
    valueCount+=1

def pairInsert(rounds):
    global valueCount
    for i in range(rounds):
        print(f'Round {i+1}')
        added = 0
        temp = []

        for polIdx in range(valueCount-1):
            firstChecked = False
            firstLetter = None
            secondLetter = None

            for key, values in letters.items():
                if polIdx in values:
                    firstLetter = key
                    if firstChecked:
                        break
                    else:
                        firstChecked = True
                if polIdx+1 in values:
                    secondLetter = key
                    if firstChecked:
                        break
                    else:
                        firstChecked = True

            for idx, rule in enumerate(insertion_rules):
                value1 = letters[rule[0][0]]
                value2 = letters[rule[0][1]]

                if [] in [value1, value2]:
                    continue
                else:
                    if rule[0][0] == firstLetter:
                        if rule[0][1] == secondLetter:
                            added +=1
                            temp.append([polIdx+added, rule[1]])

        for item in temp:
            for key,values in letters.items():
                letters[key] = [i+1 if i>=item[0] else i for i in values] 
                if key == item[1]:
                    letters[key].append(item[0])

        valueCount+= added




# Part1
pairInsert(10)
maxValue = 0
minValue = np.iinfo(uint64).max

for key, values in letters.items():
    if len(values) > maxValue:
        maxValue = len(values)
    if len(values) < minValue:
        minValue = len(values)

print(f'Part 1 {maxValue-minValue}')





