import sys

# s = """2
# 2
# 1 2
# 3
# 5 10 25
# """
s = sys.stdin.read()
import math


def solve(data, lenght):
    data_list = map(int, data.split())
    d = 0
    for x in data_list:
        d = math.gcd(d, x)
    print(x // d)   


lines = s.split("\n")

for index in range(1, len(lines) - 2, 2):
    lenght = int(lines[index])
    data = lines[index + 1]
    solve(data, lenght)
