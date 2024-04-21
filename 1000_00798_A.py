import sys


# Reading input
s = """abcfcaa
"""
# s = """fccf
# """
# s = sys.stdin.read() # submit

lines: list = s.split("\n")  # dev
first_line = lines[0]

# check palindrome
result = 0
n = len(first_line)
first_half = first_line[: n // 2]
second_half = first_line[n // 2 + n % 2 :]
second_half = second_half[::-1]
for first_char, second_char in zip(first_half, second_half):
    if first_char != second_char:
        result += 1
    if result > 1:
        break
if result == 0:
    print("NO")
elif result > 1:
    print("NO")
else:
    print("YES")
