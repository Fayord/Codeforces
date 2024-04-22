import sys

s = """5
1
9
2
14 2
7
1 2 3 4 5 6 7
6
1 3 5 7 9 11
4
2 2 2 2
"""
# s = """4 190
# """
# s = """10 135
# """
s = sys.stdin.read() # submit

lines: list = s.split("\n")  # dev
lines = lines[1:-1]
# every 2 line
map_dict = {}
for i in range(0, len(lines), 2):
    a = list(map(int, lines[i + 1].split()))
    sum_a = sum(a)
    # if sum_a is root of integer
    if sum_a in map_dict:
        print("YES")
        continue
    root = sum_a**0.5
    if root == int(root):
        map_dict[sum_a] = a

        print("YES")
    else:
        print("NO")
