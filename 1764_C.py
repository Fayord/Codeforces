import sys

s = """4
4
2 2 3 1
6
5 2 3 1 5 2
12
7 2 4 9 1 4 6 3 7 4 2 3
4
1000000 1000000 1000000 1000000
10
159699 1000000 159699 159699 159699 159699 443542 443542 159699 107374
10
1 2 3 4 5 6 7 8 9 10
5
1 2 3 4 5
"""
# s = sys.stdin.read()
import math


def solve(data, lenght):
    data_list = [int(i) for i in data.split()]
    data_list.sort()
    if data_list[0] == data_list[-1]:
        print(lenght // 2)
        return
    ans = 0
    for i in range(1, lenght):
        if data_list[i] != data_list[i - 1]:
            print("i * (lenght - i)", i, i * (lenght - i))
            print()
            ans = max(ans, i * (lenght - i))
    print(ans)


lines = s.split("\n")

for index in range(1, len(lines) - 2, 2):
    lenght = int(lines[index])
    data = lines[index + 1]
    solve(data, lenght)

# 3
# 9
# 35
# 2
