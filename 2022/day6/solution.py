with open('input.txt', 'r') as f:
  data = f.read()


def solution(data, distinct):
  for idx in range(len(data)-distinct):
    chars = set()

    for y in data[idx:idx+distinct]:
      chars.add(y)
    
    if len(chars) == distinct:
      return idx + distinct

# Part 1 and part 2
print(solution(data, 4))
print(solution(data, 14))
