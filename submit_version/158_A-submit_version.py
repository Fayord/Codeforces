import sys

s = """8 5
10 9 8 7 7 7 5 5
"""
s = """4 2
0 0 0 0
"""
s = """5 5
1 1 1 1 1
"""
# s = sys.stdin.read()
lines = s.split("\n")

ith_place = int(lines[0].split()[-1]) - 1
line = lines[1]
line_list = line.split()
ith_place_score = int(line_list[ith_place])
result = 0
for score in line_list:
    score = int(score)
    if score >= ith_place_score and score > 0:
        result += 1
    else:
        break
print(result)
