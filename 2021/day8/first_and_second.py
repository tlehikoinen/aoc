import time
import numpy as np

start_time = time.time()
with open('input.txt', 'r') as f:
    lines = [line.strip().split('|') for line in f.readlines()]

numberAppearances = np.zeros(10, int)
totalCountForNumbers = 0
segmentValue = {
        0:['a','b','c','e','f','g'],
        1:['c','f'],
        2:['a','c','d','e','g'],
        3:['a','c','d','f','g'],
        4:['b','c','d','f'],
        5:['a','b','d','f','g'],
        6:['a','b','d','e','f','g'],
        7:['a','c','f'],
        8:['a','b','c','d','e','f','g'],
        9:['a','b','c','d','f','g'],
        }

def solveSegments(patterns):
    seg = {"a":None,"b":None,"c":None,"d":None,"e":None,"f":None,"g":None,}
    segments = ['a','b','c','d','e','f','g']
    # Groups different numbers by segment count
    index_num = {2:[], 3:[], 4:[], 5:[], 6:[], 7:[],}

    for idx, p in enumerate(patterns):
        index_num[len(p)].append(idx)

    # Segment A by comparing numbers 7 and 1
    for item in patterns[index_num[3][0]]:
        for letter in item:
            if letter not in patterns[index_num[2][0]]:
                seg["a"] = letter
    
    # Segments C and F by comparing number 1 with segment length 6 numbers
    for num in index_num[6]:
        one = patterns[index_num[2][0]]
        tempLet = []
        compare = patterns[num]
        for p in compare:
            if p in one:
                tempLet.append(p)
        if len(tempLet) == 1:
            seg["f"] = tempLet[0]
            for item in patterns[index_num[2][0]]:
                if item != tempLet[0]:
                    seg["c"] = item
            break

    # Segment G by subtracting number 4's segments from numbers
    # with segment count of 6 and the one with 2 segments left is 9, 
    # then remove a (known) to get remaining g
    for num in index_num[6]:
        four = patterns[index_num[4][0]]
        tempLet = []
        compare = patterns[num]
        for p in compare:
            if p not in four:
                tempLet.append(p)
        if len(tempLet) == 2:
            for let in tempLet:
                if let != seg["a"]:
                    seg["g"] = let
            break

    # Segment B by subtracting currently known segments from numbers 
    # with segment count of 6, sum remaining segments together and 
    # the one with +3 is b segment
    tempSeg = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,}
    curValues = [i for key, i in seg.items()]
    for num in index_num[6]:
        compare=patterns[num]
        tempList = [i for i in compare]
        for p in compare:
            if p in curValues:
                tempList.remove(p)
        for item in tempList:
            tempSeg[item] +=1

    # Max (3) is the b segment
    seg["b"] = max(tempSeg, key=tempSeg.get)

    # Segment D by subtracting currently known segments from numbers with 
    # segment count of 5
    tempSeg = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,}
    curValues = [i for key, i in seg.items()]
    for num in index_num[5]:
        compare=patterns[num]
        tempList = [i for i in compare]
        for p in compare:
            if p in curValues:
                tempList.remove(p)
        for item in tempList:
            tempSeg[item] +=1

    seg["d"] = max(tempSeg, key=tempSeg.get)

    # 6 segments are known. Find the remaining one
    empty = None
    for key, value in seg.items():
        if value != None:
            segments.remove(value)
        else:
            empty = key
    # Assign remaining one to empty key
    seg[empty] = segments[0]

    # Return decrypted dictionary
    return seg

def solverA(seg,values):
    global totalCountForNumbers
    allNums = []
    for number in values:
        falseSeg = []
        for n in number:
            for key, value in seg.items():
                if value == n:
                    falseSeg.append(key)
                    break

        falseSeg.sort()
        for key, value in segmentValue.items():
            #value.sort()
            if falseSeg == value:
                allNums.append(key)
                numberAppearances[key] +=1
                break
            else:
                pass
    sumForNums = 0
    length = len(allNums)-1
    for n in allNums:
        sumForNums += n*(10**length)
        length -=1
    totalCountForNumbers += sumForNums


for line in lines:
    #print("NEW")
    line[0] = line[0].strip().split(' ')
    line[1] = line[1].strip().split(' ')
    seg = solveSegments(line[0])
    solverA(seg, line[1])

print("Number of appearances for each number (index=num)\n" + str(numberAppearances))
print("Total count of sums\n" + str(totalCountForNumbers))
    
print("--- %s seconds ---" % (time.time() - start_time))


