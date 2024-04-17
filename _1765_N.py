import sys
import numpy as np

s = """5
10000
4
1337
0
987654321
6
66837494128
5
7808652
3
"""
s = """5
1337
0
987654321
6
66837494128
5
7808652
3
"""
# s = sys.stdin.read()
lines = s.split("\n")


def solve(data, target):
    data_lenght = len(data)
    if target == 0:
        print(data)
        return

    result = ""
    data_split = list(data)
    target = data_lenght - target
    print("data_lenght", data_lenght)
    print("target", target)
    for i in range(target):
        if result == "":
            print("candidate :", data_split[: -target + 1])
            candidate = [i for i in data_split[: -target + 1] if i != "0"]
            print("first candidate :", candidate)

        else:
            candidate = data_split[min_candidate_index + 1 : min_candidate_index + 2]
            print("candidate", candidate)
        min_candidate_index = np.argmin(candidate)
        result = result + candidate[min_candidate_index]
    print("result", result)


for index in range(1, len(lines) - 2, 2):
    data = lines[index]
    target = int(lines[index + 1])
    print(data)
    print("target", target)
    solve(data, target)
    print()
# 1
# 1337
# 321
# 344128
# 7052


# def rl():
#     return list(map(int, input().split()))

# # Since k < len(x), we can always successfully use all k
# # removals in at least one way (x starts with a non-zero digit;
# # delete everything else).
# # Thus, the optimal answer must use all k removals, since shorter
# # numbers are smaller (b/c we don't deal with leading 0s). This
# # means all contenders for optimal answer are of the same length
# # with no leading 0's, so we are just comparing lexicographically.
# #
# # If it is possible to start an answer with 1, we must (typical lex. sorting
# # logic). Given that, it is always optimal to prefer the "leftmost" 1, because
# # it gives strictly more flexibility in choosing the remaining suffix.
# #
# # Then, we can sort of repeat this with binary search and 10
# # arrays of indices, one for each digit

# def solve():
#     x = input()
#     k = ri()
#     n = len(x)
#     j = n - k

#     I = [list() for i in range(10)]
#     for i in range(n):
#         I[int(x[i])].append(i)

#     J = [0] * 10 # 10-pointer technique ;)

#     def feasible(index, n, remaining):
#         return remaining <= n - index

#     # starting digit cannot be 0
#     last_used_index = -1
#     for d in range(1, 10):
#         if J[d] >= len(I[d]):
#             continue
#         index = I[d][J[d]]
#         if feasible(index, n, j):
#             print (d, end = "")
#             last_used_index = I[d][J[d]]
#             J[d] += 1
#             j -= 1
#             break

#     # rest of digits can be 0
#     while j:
#         for d in range(10):
#             # must go in order
#             while J[d] < len(I[d]) and I[d][J[d]] <= last_used_index:
#                 J[d] += 1

#             if J[d] >= len(I[d]):
#                 continue
#             index = I[d][J[d]]
#             if feasible(index, n, j):
#                 print(d, end = "")
#                 last_used_index = I[d][J[d]]
#                 J[d] += 1
#                 j -= 1
#                 break
#     print ()
