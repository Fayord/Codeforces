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
m = len(grid)
n = len(grid[0])

# Initialize dp matrix
dp_2 = [[0] * n for _ in range(m)]
dp_5 = [[0] * n for _ in range(m)]
dp_2[0][0] = grid[0][0]
dp_5[0][0] = grid[0][0]
directions_grid = [[""] * n for _ in range(m)]

# Fill the first row
for j in range(1, n):
    directions_grid[0][j] = "R" * j
    dp_2[0][j] = dp_2[0][j - 1] * grid[0][j]
    dp_5[0][j] = dp_5[0][j - 1] * grid[0][j]

# Fill the first column
for i in range(1, m):
    directions_grid[i][0] = "D" * i
    dp_2[i][0] = dp_2[i - 1][0] * grid[i][0]
    dp_5[i][0] = dp_5[i - 1][0] * grid[i][0]
# Fill the rest of the dp matrix
for i in range(1, m):
    for j in range(1, n):
        choice1 = dp_2[i - 1][j] * grid[i][j]
        choice2 = dp_2[i][j - 1] * grid[i][j]
