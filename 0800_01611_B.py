import sys

s = """6
5 5
10 1
2 3
0 0
17 2
1000000000 1000000000
"""
# s = """4 190
# """
# s = """10 135
# """
# s = sys.stdin.read() # submit

lines: list = s.split("\n")  # dev
lines = lines[1:-1]

for line in lines:
    a, b = list(map(int, line.split()))
    if a == 0 or b == 0:
        print(0)
        continue
    min_team = min(a, b)
    max_team = max(a, b)
    ratio = max_team / min_team

    if ratio <= 3:
        member = min_team + max_team
    else:
        member = min_team * 4
    all_team = member // 4
    # remain = a + b
    # new_team = remain // 4
    # all_team += new_team
    print(all_team)
