import sys
from functools import wraps

s = """100
195676
357095
540959
30764
37882
867304
418165
473724
636762
374239
59598
903199
577079
7848
713425
283798
277703
255270
202413
533360
128164
783573
527368
48418
611953
241245
921984
528925
384398
924178
488637
647747
700718
448439
735044
992812
212479
695984
887565
33873
282123
508661
258174
372413
359132
314096
121880
307133
448003
225672
255414
483018
310187
887369
9340
804726
494638
468935
355086
111182
247946
494344
"""

# s = sys.stdin.read()
lines = s.split("\n")


def memorize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


import math


def solve(n):
    if n % 2 == 0:
        print(n // 2, n // 2)
        return
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(n // i, n - n // i)
            return
    print(1, n - 1)


for line in lines[1:-1]:
    pair_list = []
    data = int(line)
    solve(data)
    # print("\n" * 5)
# 1 1
# 3 6
# 1 4
# 5 5
