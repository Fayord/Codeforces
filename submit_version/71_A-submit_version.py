import sys

s = """1
1000000000 999999999 999999999 999999998
"""
# s = sys.stdin.read()
lines = s.split("\n")

for line in lines[1:-1]:
    word = line.split()[0]
    lenght = len(word)
    if lenght > 10:
        word = word[0] + str(lenght - 2) + word[-1]

    print(word)
