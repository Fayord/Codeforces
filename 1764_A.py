import sys

# s = """7
# 5
# 1 3 2 2 4
# 5
# 1 2 3 4 5
# 4
# 2 1 2 1
# 3
# 2 3 3
# 2
# 2 2
# 1
# 1
# 9
# 9 8 5 2 1 1 2 3 3
# """
s = sys.stdin.read()


lines = s.split("\n")

for index in range(1, len(lines) - 2, 2):
    lenght = int(lines[index])
    data = lines[index + 1]
    print(1, lenght)
