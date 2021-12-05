with open('input.txt') as f:
    lines = f.readlines()

temp = lines[0]
counter = 1
for line in lines[1:]:
    if line > temp:
        counter+=1
    temp = line

print(counter)
