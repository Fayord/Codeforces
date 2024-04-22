import sys

s = """3 222
"""
# s = """4 190
# """
# s = """10 135
# """
# s = sys.stdin.read() # submit

lines: list = s.split("\n")  # dev
max_n, k = list(map(int, lines[0].split()))
n = 5
total_time = 240
remain_time = total_time - k
remain_time = remain_time / 5
import math

q = (-1 + math.sqrt(1 + (4 * 2 * remain_time))) / 2
q = math.floor(q)
if q > max_n:
    q = max_n
# print(n, k)
print(q)
# print(result)
