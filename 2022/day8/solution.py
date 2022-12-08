with open('input.txt', 'r') as f:
  data = [l.strip() for l in f.readlines()]

def solution_part1(data):

  ans = (len(data[0]) * 2 + (len(data)-2) * 2)

  for x in range(1, len(data)-1):
    for y in range(1, len(data[x])-1):
      num = data[x][y]
      visible = False

      upCount = 0
      for up in range(0, x):
        if data[up][y] < num:
          upCount += 1
      if upCount == len(data[:x]):
        visible = True

      downCount = 0
      for down in range(x+1, len(data)):
        if data[down][y] < num:
          downCount += 1
      if downCount == len(data[x+1:]):
        visible = True

      rightCount = 0
      for right in range(y+1, len(data[x])):
        if data[x][right] < num:
          rightCount += 1
      if rightCount == len(data[x][y+1:]):
        visible = True

      leftCount = 0
      for left in range(0, y):
        if data[x][left] < num:
          leftCount += 1
      if leftCount == len(data[:y]):
        visible = True

      if visible:
        ans += 1
  

  print(f'Part 1 answer = {ans}')

def solution_part2(data):

  highest_scenic = { "x": '0', "y": '0', "ans": 0 }


  for x in range(len(data)):
    for y in range(len(data[x])):
      num = data[x][y]

      upCount = 0
      for up in range(x-1, -1, -1):
        upCount += 1
        if data[up][y] >= num:
          break

      downCount = 0
      for down in range(x+1, len(data)):
        downCount += 1
        if data[down][y] >= num:
          break

      rightCount = 0
      for right in range(y+1, len(data[x])):
        rightCount += 1
        if data[x][right] >= num:
          break

      leftCount = 0
      for left in range(y-1, -1, -1):
        leftCount += 1
        if data[x][left] >= num:
          break

      scenic = downCount * upCount * rightCount * leftCount

      if scenic > highest_scenic['ans'] :
        highest_scenic['x'] = x
        highest_scenic['y'] = y
        highest_scenic['ans'] = scenic

  print(f'Part 2 answer = {highest_scenic}')



solution_part1(data)
solution_part2(data)
