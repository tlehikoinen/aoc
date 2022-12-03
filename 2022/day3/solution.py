with open('input.txt', 'r') as f:
  data = [l.strip() for l in f.readlines()]

# Part 1
sum = 0
for l in data:
  lenght = int(len(l)/2)
  left = l[:lenght]
  right = l[lenght:]

  for c in left:
    if c in right:
      if ord(c) > 96:
        sum += ord(c) -96
      else:
        sum += ord(c) -38
      break

print(f'Part 1 = {sum}')



# Part 2
sum2 = 0
for i in range(0, len(data), 3):
  for y in data[i]:
    if y in data[i+1] and y in data[i+2]:
      if ord(y) > 96:
        sum2 += ord(y) -96
      else:
        sum2 += ord(y) -38
      break

print(f'Part 2 = {sum2}')
