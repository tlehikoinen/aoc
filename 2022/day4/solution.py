with open('input.txt', 'r') as f:
  data = [l.strip() for l in f.readlines()]


# Part 1
def solution_part1(data):
  sum = 0
  for line in data:
    left, right = [l.split('-') for l in line.split(',')]

    left = [int(i) for i in left]
    right = [int(i) for i in right]

    if ((left[0] >= right[0] and left[1] <= right[1]) or \
      (right[0] >= left[0] and right[1] <= left[1])):
      sum += 1

  return sum


# Part 2
def solution_part2(data):
  sum = 0
  for line in data:
    left, right = [l.split('-') for l in line.split(',')]

    left = [int(i) for i in left]
    right = [int(i) for i in right]

    if (left[0] >= right[0] and left[0] <= right[1]) or \
      (left[1] >= right[0] and left[0] <= right[1]) or \
      (right[0] >= left[0] and right[1] <= left[1]) or \
      (right[1] >= left[0] and right[1] <= left[1]):
      sum += 1

  return sum

# Print solutions
print(f'Part 1 = {solution_part1(data)}')
print(f'Part 2 = {solution_part2(data)}')