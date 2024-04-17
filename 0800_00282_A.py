import sys

s = """1
++X"""
# s = sys.stdin.read() # submit
lines: list = s.split("\n")  # dev
result = 0
for line in lines[1:]:
    if "++" in line:
        result += 1
    elif "--" in line:
        result -= 1
print(result)
