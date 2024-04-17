def least_round_way(matrix):
    """
    Finds the path with the least number of trailing zeros in the product.

    Args:
        matrix: A 2D list representing the square matrix of non-negative integers.

    Returns:
        A tuple containing:
            - min_zeros: The minimum number of trailing zeros.
            - path: A string representing the path (combination of 'D' and 'R').
    """

    n = len(matrix)
    dp_2 = [[float("inf")] * n for _ in range(n)]  # Minimum sum for 2's
    dp_5 = [[float("inf")] * n for _ in range(n)]  # Minimum sum for 5's

    # Base cases for top row and leftmost column
    for i in range(n):
        dp_2[0][i] = matrix[0][i] if matrix[0][i] % 2 else float("inf")
        dp_5[i][0] = matrix[i][0] if matrix[i][0] % 5 else float("inf")

    # Dynamic programming for 2's and 5's
    for i in range(1, n):
        for j in range(1, n):
            dp_2[i][j] = (
                min(dp_2[i - 1][j], dp_2[i][j - 1]) + matrix[i][j]
                if matrix[i][j] % 2
                else float("inf")
            )
            dp_5[i][j] = (
                min(dp_5[i - 1][j], dp_5[i][j - 1]) + matrix[i][j]
                if matrix[i][j] % 5
                else float("inf")
            )

    # Check if a path with no trailing zeros exists
    if dp_2[n - 1][n - 1] != float("inf") and dp_5[n - 1][n - 1] != float("inf"):
        min_zeros = 0
        path = reconstruct_path(
            dp_2, n - 1, n - 1, "D", "R"
        )  # Prefer path with no trailing zeros
    else:
        # Find minimum between 2's and 5's paths (one with trailing zeros)
        min_zeros = (
            min(dp_2[n - 1][n - 1], dp_5[n - 1][n - 1]) // 5
        )  # Count trailing zeros for the min path
        if dp_2[n - 1][n - 1] < dp_5[n - 1][n - 1]:
            path = reconstruct_path(dp_2, n - 1, n - 1, "D", "R")
        else:
            path = reconstruct_path(dp_5, n - 1, n - 1, "D", "R")

    return min_zeros, path


def reconstruct_path(dp, i, j, down_dir, right_dir):
    """
    Reconstructs the path string from the dynamic programming table.

    Args:
        dp: The 2D list representing the dynamic programming table.
        i: Row index in the table.
        j: Column index in the table.
        down_dir: Character representing the down direction ('D').
        right_dir: Character representing the right direction ('R').

    Returns:
        A string representing the path (combination of 'D' and 'R').
    """

    if i == 0:
        return right_dir * j
    elif j == 0:
        return down_dir * i
    else:
        if dp[i][j] == dp[i - 1][j] + dp[i][j]:
            return down_dir + reconstruct_path(dp, i - 1, j, down_dir, right_dir)
        else:
            return right_dir + reconstruct_path(dp, i, j - 1, down_dir, right_dir)


# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
min_zeros, path = least_round_way(matrix)
print(f"Least number of trailing zeros: {min_zeros}")
print(f"Path with least trailing zeros: {path}")
