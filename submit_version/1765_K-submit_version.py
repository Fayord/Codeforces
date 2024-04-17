import sys

# s = """3
# 0 0 1000000000
# 0 1000000000 0
# 1000000000 0 0
# """
# s = """2
# 1 2
# 3 4
# """
# s = """3
# 10 10 10
# 10 0 10
# 10 10 10
# """
s = sys.stdin.read()


def solve(cell_data, n):
    result = sum(cell_data)
    select_cell = cell_data[n - 1 : -1 : n - 1]
    # print(select_cell)
    find_lowest_cell = min(select_cell)
    result = result - find_lowest_cell
    print(result)


lines = s.split("\n")
cell_data = []
for line in lines[1:-1]:
    row_data = [int(i) for i in line.split()]

    cell_data.extend(row_data)
n = len(row_data)
solve(cell_data, n)
