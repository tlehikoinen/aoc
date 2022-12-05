with open('input.txt', 'r') as f:
  data = [l.strip() for l in f.readlines()]


def solution_part1(data):
  # Find bottom line (containing line numbers)
  num = 0
  while '[' in data[num]:
    num+=1

  # Create a dictionary that holds lines as keys and lists as value
  lines = {int(i): [] for i in data[num].split('   ')}

  # Create initial dictionary state
  for i in data[num-1::-1]:
    for idx, l in enumerate(i[1::4]):
      if l != ' ':
        lines[idx+1].append(l)

  # Loop through instructions
  for i in data[num+2::]:
    line = i.split(' ')

    for _ in range(int(line[1])):
      try:
        removed = lines[int(line[3])].pop()
        lines[int(line[5])].append(removed)
      except:
        continue

  ans = ""
  for i in lines.keys():
    ans += lines[i][-1]
  print(f'Part 1 solution = {ans}')


def solution_part2(data):
  # Find bottom line (containing line numbers)
  num = 0
  while '[' in data[num]:
    num+=1

  # Create a dictionary that holds lines as keys and lists as value
  lines = {int(i): [] for i in data[num].split('   ')}

  # Create initial dictionary state
  for i in data[num-1::-1]:
    for idx, l in enumerate(i[1::4]):
      if l != ' ':
        lines[idx+1].append(l)

  # Loop through instructions
  for i in data[num+2::]:
    line = i.split(' ')
    end_of_list = []

    for y in range(int(line[1]), 0, -1):
      try:
        num = lines[int(line[3])].pop(-y)
        end_of_list.append(num)
      except:
        continue

    lines[int(line[5])].extend(end_of_list)

  ans = ""
  for i in lines.keys():
    ans += lines[i][-1]
  print(f'Part 2 solution = {ans}')

solution_part1(data)
solution_part2(data)
