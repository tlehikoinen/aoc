import sys
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
days = 80
for i in range(days):
    for index in range(len(data)):
        data[index] -=1
        if data[index] == -1:
            data.append(8)
            data[index] = 6
    
print("RESULT =\n" + str(len(data)))

