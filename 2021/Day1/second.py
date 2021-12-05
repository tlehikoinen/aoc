with open('input.txt') as f:
    lines = f.readlines()

lines = [int(i) for i in lines]
def returnSumOfThree(array, index):
    sumOfThree = sum(array[index:index+3])
    return sumOfThree

counter = 1
temp = returnSumOfThree(lines, 1)
for i in range(1,len(lines)):
    count = returnSumOfThree(lines, int(i))
    if count > temp:
        counter+=1
    temp = count

print(counter)
