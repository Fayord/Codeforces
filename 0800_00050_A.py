import sys

s = """1
++X"""
# s = sys.stdin.read() # submit
lines: list = s.split("\n")  # dev
first_line = lines[0]
m, n = map(int, first_line.split())
result = m * n // 2
print(result)
