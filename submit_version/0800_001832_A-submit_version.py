import sys


# Reading input
s = """3
codedoc
gg
aabaa
"""
s = sys.stdin.read() # submit

lines: list = s.split("\n")  # dev
lines = lines[1:-1]


def can_it_create_new_palindrome(s: str) -> None:
    first_half = s[: len(s) // 2]
    # check that first_half have more than 1 different character
    if len(set(first_half)) > 1:
        print("YES")
    else:
        print("NO")


for line in lines:
    can_it_create_new_palindrome(line)
