with open('input.txt', 'r') as f:
  data = [i.strip() for i in f.readlines()]

elves_snacks = []

snacks = []
for l in data:
  if l != '':
    snacks.append(int(l))
  else:
    elves_snacks.append(snacks)
    snacks = []

sum_snacks = [sum(i) for i in elves_snacks]
sum_snacks.sort(reverse=True)

# Part 1
print(sum_snacks[0])

# Part 2
print(sum(sum_snacks[0:3]))
