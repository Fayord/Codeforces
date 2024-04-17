import sys

# s = """4
# 4
# ossu
# 2
# aa
# 6
# addonn
# 3
# qwe
# """
s = sys.stdin.read()


def solve(data, lenght):
    if lenght % 3 != 0 and (lenght - 1) % 3 != 0:
        print("NO")
        return
    for i in range(int(lenght // 3)):
        if data[i * 3 + 1] != data[i * 3 + 2]:
            print("NO")
            return

    print("YES")


lines = s.split("\n")
cell_data = []

for index in range(1, len(lines) - 2, 2):
    lenght = int(lines[index])
    data = lines[index + 1]
    solve(data, lenght)
    # print()
