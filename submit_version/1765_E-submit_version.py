import sys
from functools import wraps

# s = """4
# 100 25 30
# 9999997 25 50
# 52 50 48
# 49 50 1
# """
s = sys.stdin.read()
lines = s.split("\n")

import math


def memorize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


def cal_ceil(a, b):
    return math.ceil(a / b)


def solve(a, b, c):
    if c < b:
        print(1)
        return
    result = cal_ceil(a, b)
    print(result)


for line in lines[1:-1]:
    a, b, c = map(int, line.split())
    solve(a, b, c)
# 4
# 400000
# 1
# 1
