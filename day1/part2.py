digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
mapping = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

f = open("./input.txt", "r")
lines = f.readlines()

def findDigit(line: str):
  for digit in digits:
    idx = line.find(digit)
    if idx != -1:
      return mapping[digit]
  return False

res = 0
for line in lines:
  line = line.strip()
  l, r = 0, 0
  i = 0
  # cursed o(n^n) time complexity probably, dear god
  while i < len(line) and not l:
    if line[i].isdigit():
      l = line[i]
    else:
      curr = findDigit(line[:i+1])
      if curr:
        l = curr
    i += 1
  
  i = len(line) - 1
  while i > -1 and not r:
    if line[i].isdigit():
      r = line[i]
    else:
      curr = findDigit(line[i:])
      if curr:
        r = curr
    i -= 1
  res += (int(l) * 10) + int(r)
print(res)