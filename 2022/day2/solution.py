with open('input.txt', 'r') as f:
  data = [l.strip() for l in f.readlines()]

# Part 1
results = {
  'A': { 'X': 3 + 1, 'Y': 6 + 2, 'Z': 0 + 3 },
  'B': { 'X': 0 + 1, 'Y': 3 + 2, 'Z': 6 + 3 },
  'C': { 'X': 6 + 1, 'Y': 0 + 2, 'Z': 3 + 3 },
}

sum = 0
for d in data:
  sum += results[d[0]][d[2]]

print(f'Part 1 = {sum}')

# Part 2
results2 = {
  'A': { 'X': 'Z', 'Y': 'X', 'Z': 'Y' },
  'B': { 'X': 'X', 'Y': 'Y', 'Z': 'Z' },
  'C': { 'X': 'Y', 'Y': 'Z', 'Z': 'X' },
}


sum2 = 0
for d in data:
  sum2 += results[d[0]][results2[d[0]][d[2]]]

print(f'Part 2 = {sum2}')


