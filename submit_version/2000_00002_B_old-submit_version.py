import sys

s = """3
1 2 3
4 5 6
7 8 9
"""
# expected_output = """aawtvezfntstrcpgbzjbf"""
s = sys.stdin.read() # submit

lines: list = s.split("\n")  # dev
lines = lines[1:-1]
n = len(lines)

grid = []
for line in lines:
    grid.append(list(map(int, line.split())))
# print(grid)


def get_trailing_zeros(longint):
    manipulandum = str(longint)
    # if last digit is 5 +0.5
    trim_zero = manipulandum.rstrip("0")
    extra = 0
    if trim_zero[-1] == "5":
        extra = 0.5
    # if last digit is even number +0.2
    if int(trim_zero[-1]) % 2 == 0:
        extra = 0.6
    return len(manipulandum) - len(trim_zero), extra


from typing import List, Tuple

# print(grid)


def least_trailing_zero(grid: List[List[int]]) -> Tuple[int, str]:
    m = len(grid)
    n = len(grid[0])

    # Initialize dp matrix
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    directions_grid = [[""] * n for _ in range(m)]

    # Fill the first row
    for j in range(1, n):
        directions_grid[0][j] = "R" * j
        dp[0][j] = dp[0][j - 1] * grid[0][j]

    # Fill the first column
    for i in range(1, m):
        directions_grid[i][0] = "D" * i
        dp[i][0] = dp[i - 1][0] * grid[i][0]
    # Fill the rest of the dp matrix
    for i in range(1, m):
        for j in range(1, n):
            choice1 = dp[i - 1][j] * grid[i][j]
            choice2 = dp[i][j - 1] * grid[i][j]
            trailing_zero_1, extra_1 = get_trailing_zeros(choice1)
            trailing_zero_2, extra_2 = get_trailing_zeros(choice2)
            if trailing_zero_1 + extra_1 <= trailing_zero_2 + extra_2:
                dp[i][j] = choice1
                directions_grid[i][j] = directions_grid[i - 1][j] + "D"

            else:
                dp[i][j] = choice2
                directions_grid[i][j] = directions_grid[i][j - 1] + "R"
    trailing_zero, _ = get_trailing_zeros(dp[m - 1][n - 1])
    directions = directions_grid[m - 1][n - 1]
    # print(directions_grid)
    return trailing_zero, directions


def min_sum_path(A):
    # Dimensions of the square
    n = len(A)

    # Initialize DP table with zeros
    D = [[0] * n for _ in range(n)]

    # Initialize first row and first column of DP table
    D[0][0] = A[0][0]
    for i in range(1, n):
        D[i][0] = D[i - 1][0] + A[i][0]
        D[0][i] = D[0][i - 1] + A[0][i]

    # Fill DP table
    for i in range(1, n):
        for j in range(1, n):
            D[i][j] = min(D[i - 1][j], D[i][j - 1]) + A[i][j]

    return D[n - 1][n - 1]


def least_round_way(square):
    # Replace all 0's with 10's
    for i in range(len(square)):
        for j in range(len(square[0])):
            if square[i][j] == 0:
                square[i][j] = 10

    # Solve for both 2's and 5's
    min_sum_2s = min_sum_path(square)

    # Transpose the square to solve for 5's
    square_transpose = [[row[i] for row in square] for i in range(len(square[0]))]
    min_sum_5s = min_sum_path(square_transpose)

    # Return the minimum of the two solutions
    return min(min_sum_2s, min_sum_5s)


# Example usage:
square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Minimum sum for least round way:", least_round_way(square))

# trailing_zero, directions = least_trailing_zero(grid)
# print(trailing_zero)
# print(directions)
