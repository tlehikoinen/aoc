import collections
from numpy import uint64
import numpy as np
with open('input.txt','r') as f:
    data = f.read().strip().split('\n')

polymer = data[0]
insertion_rules =[[i[0],i[1]] for i in [item.split(' -> ') for item in data[2:]]]

# letters keep count for letter appearances
letters = collections.defaultdict(uint64)
#letters2 = collections.defaultdict(uint64)

for l in insertion_rules:
    letters[l[0][0]] = 0
    letters[l[0][1]] = 0
    #letters2[l[0][0]] = 0
    #letters2[l[0][1]] = 0

for l in polymer:
    letters[l] += 1

# pairs keep track of the different pairs 
pairs = collections.defaultdict(uint64)
for idx in range(len(polymer)-1):
    if pairs[f'{polymer[idx]}{polymer[idx+1]}']:
        pairs[f'{polymer[idx]}{polymer[idx+1]}'] += 1
    else:
        pairs[f'{polymer[idx]}{polymer[idx+1]}'] = 1
    
def pairInsert(steps):
    global letters
    for r in range(steps):
        tempDel = []
        temp = collections.defaultdict(int)
        for pair in pairs.keys():
            for rule in insertion_rules:
                if pair == rule[0]: 
                    new_1 = f'{rule[0][0]}{rule[1]}'
                    new_2 = f'{rule[1]}{rule[0][1]}'
                    # Increase the count only for the new letter
                    letters[rule[1]] += pairs[pair]

                    # Save new pairs to temp dict to be appended at the end of the round
                    if new_1 in temp: temp[new_1] += pairs[pair]
                    else: temp[new_1] = pairs[pair] 

                    if new_2 in temp: temp[new_2] += pairs[pair] 
                    else: temp[new_2] = pairs[pair] 

                    # Save pairs that need to be deleted at the end of the round 
                    if pair not in [new_1, new_2]: tempDel.append(pair)

                    pairs[pair] = 0

        for key,values in temp.items():
            if pairs[key]: pairs[key] += values
            else: pairs[key] = values

        for t in tempDel:
            if t not in temp:
                pairs.pop(t)

        #print(pairs)
        #print(f'COUNTER {sum(pairs.values())+1}')

# Part2
pairInsert(40)

maxValue = 0
minValue = np.iinfo(uint64).max

# another way to calculate object apperances
#for key, value in pairs.items():
#    letters2[key[0]] += value
#    letters2[key[1]] += value
#print(f'Result {(maxValue-minValue)//2+1}')

for i in letters.values():
    #print("letter value")
    #print(i)
    if i > maxValue:
        maxValue = i
    if i < minValue:
        minValue = i

#print(pairs)
#print(len(pairs.values()))
print(f'Part2 result = {(maxValue-minValue)}')



