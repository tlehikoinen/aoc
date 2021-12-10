with open('input.txt', 'r') as f:
    data = f.readlines()

startChars = ['(', '[', '{', '<']
endChars = [')', ']', '}', '>']
charDict= {'(':')', '[':']', '{':'}', '<':'>'}
points = {')':3, ']':57, '}':1197, '>':25137}
broken = 0
pointsCount = 0
for d in data:
    start = []
    end = []
    d.split()
    for i in d:
        if i in startChars:
            start.append(i)
            end.append(charDict[i])
        elif i in endChars:
            if i != end[-1]:
                broken +=1
                pointsCount += points[i]
                break
            else:
                start.pop()
                end.pop()
    
    
print("Broken lines = " + str(broken))
print("Broken points (Part1) = " + str(pointsCount))
