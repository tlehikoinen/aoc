with open('input.txt', 'r') as f:
    data = f.readlines()

startChars = ['(', '[', '{', '<']
endChars = [')', ']', '}', '>']
charDict= {'(':')', '[':']', '{':'}', '<':'>'}
points1 = {')':3, ']':57, '}':1197, '>':25137}
points2 = {')':1, ']':2, '}':3, '>':4}
broken = 0
pointsCount = 0

incompleteEndings = []
for d in data:
    start = []
    end = []
    d.split()
    for idx, i in enumerate(d):
        if i in startChars:
            start.append(i)
            end.append(charDict[i])
        elif i in endChars:
            if i != end[-1]:
                broken +=1
                # Part1 points
                pointsCount += points1[i]
                break
            else:
                start.pop()
                end.pop()

        if idx == len(d)-1:
            incompleteEndings.append(end)

# Part2 points
autoCompPoints = []
for line in incompleteEndings:
    print(line)
    temp = 0
    # Iterates from the last to first
    for i in range(len(line)-1, -1, -1):
        temp *= 5
        temp += points2[line[i]]
    autoCompPoints.append(temp)
    
print("Broken lines = " + str(broken))
print("Broken points (Part1) = " + str(pointsCount))
autoCompPoints.sort()
print("Middle score (Part2) = " + str(autoCompPoints[int(len(autoCompPoints)/2)]))
