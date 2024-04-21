import sys


# Reading input
s = """3
4
1001
1
0
5
10001
"""
s = sys.stdin.read() # submit

lines: list = s.split("\n")  # dev
lines = lines[1:-1]


def who_wins_game(num: str) -> str:
    # find number of 0 in str
    num_zero = num.count("0")
    # if number of 0 is even, then Bob wins
    if num_zero % 2 == 0:
        return "BOB"
    elif num_zero == 1:
        return "BOB"
    else:
        return "ALICE"


for i in range(0, len(lines), 2):
    num = lines[i + 1]
    print(who_wins_game(num))
