import sys


def max_points(a: list):
    max_num = max(a)
    freq = [0] * (max_num + 1)
    dp = [0] * (max_num + 1)

    # Step 1: Count the frequency of each number in the sequence
    for num in a:
        freq[num] += 1

    # Step 2: Initialize the base cases for dynamic programming
    dp[1] = freq[1]

    # Step 3: Compute the maximum points using dynamic programming
    for i in range(2, max_num + 1):
        # Explanation for current iteration
        print(f"Calculating maximum points for number {i}: dp :", dp)

        # Option 1: Exclude the current number
        option1 = dp[i - 1]
        print(f"Option 1: Excluding {i}, previous maximum points: {option1}")

        # Option 2: Include the current number
        option2 = dp[i - 2] + i * freq[i]
        print(
            f"Option 2: Including {i} and deleting {i} and {i - 1}, points: {option2}"
        )

        # Choose the maximum of the two options
        dp[i] = max(option1, option2)
        print(f"Choosing maximum of Option 1 and Option 2: {dp[i]},{dp}\n")

    # Step 4: Return the maximum points up to the maximum number in the sequence
    return dp[max_num]


# Reading input
s = """5
3 3 4 5 4
"""
s = sys.stdin.read() # submit

lines: list = s.split("\n")  # dev
second_line = lines[1]
a = list(map(int, second_line.split()))

# Calling function to get maximum points
result = max_points(a)

# Printing the result
print(result)
