import sys

s = """6 6 4
"""
s = sys.stdin.read() # submit
lines: list = s.split("\n")  # dev
first_line = lines[0]
m, n, a = map(int, first_line.split())
# b = m ceil a
b = (m + a - 1) // a
# c = n ceil a
c = (n + a - 1) // a
result = b * c
print(result)
