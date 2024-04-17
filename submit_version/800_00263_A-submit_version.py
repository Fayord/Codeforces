import sys

s = """0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
"""
s = sys.stdin.read() # submit
lines: list = s.split("\n")[:-1]  # dev
for row, line in enumerate(lines):
    # find index of 1 if it exists
    if "1" in line:
        col = line.index("1")
        break
col = col // 2
row -= 2
col -= 2

result = abs(row) + abs(col)
print(result)
