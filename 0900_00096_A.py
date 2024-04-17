import sys

s = """1000000001
"""
# s = sys.stdin.read() # submit
lines: list = s.split("\n")  # dev
first_line = lines[0]
result = "NO"
if first_line.find("1111111") != -1 or first_line.find("0000000") != -1:
    result = "YES"
print(result)
