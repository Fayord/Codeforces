import sys

s = """3
1 2 3
4 5 6
7 8 9
"""
# expected_output = """aawtvezfntstrcpgbzjbf"""
# s = sys.stdin.read() # submit

lines: list = s.split("\n")  # dev
lines = lines[1:-1]
n = len(lines)

grid = []
for line in lines:
    grid.append(list(map(int, line.split())))
# print(grid)

# instead of finding trailing zero we need to find mod 2 and 5
