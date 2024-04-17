def count_trailing_zeros(num):
    count = 0
    while num % 10 == 0:
        count += 1
        num //= 10
    return count


def find_least_round_way(matrix):
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    path = [[""] * n for _ in range(n)]

    # Initialize first row and column
    dp[0][0] = count_trailing_zeros(matrix[0][0])
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + count_trailing_zeros(matrix[i][0])
        dp[0][i] = dp[0][i - 1] + count_trailing_zeros(matrix[0][i])
        path[i][0] = "D"
        path[0][i] = "R"

    # Fill the dp table
    for i in range(1, n):
        for j in range(1, n):
            from_top = dp[i - 1][j] + count_trailing_zeros(matrix[i][j])
            from_left = dp[i][j - 1] + count_trailing_zeros(matrix[i][j])
            if from_top < from_left:
                dp[i][j] = from_top
                path[i][j] = "D"
            else:
                dp[i][j] = from_left
                path[i][j] = "R"

    # Construct the path
    i, j = n - 1, n - 1
    way = ""
    while i > 0 or j > 0:
        way += path[i][j]
        if path[i][j] == "D":
            i -= 1
        else:
            j -= 1
    return dp[n - 1][n - 1], way[::-1]


import sys

# Input
s = """3
1 2 3
4 5 6
7 8 9
"""
s = sys.stdin.read()  # submit

lines: list = s.split("\n")  # dev
lines = lines[1:-1]
n = len(lines)

grid = []
for line in lines:
    grid.append(list(map(int, line.split())))

# Output
least_zeros, way = find_least_round_way(grid)
print(least_zeros)
print(way)
