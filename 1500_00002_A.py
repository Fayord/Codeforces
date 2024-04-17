import sys

s = """3
mike 3
andrew 5
mike 2
"""
s = """3
andrew 3
andrew 2
mike 5
"""
s = """15
aawtvezfntstrcpgbzjbf 681
zhahpvqiptvksnbjkdvmknb -74
aawtvezfntstrcpgbzjbf 661
jpdwmyke 474
aawtvezfntstrcpgbzjbf -547
aawtvezfntstrcpgbzjbf 600
zhahpvqiptvksnbjkdvmknb -11
jpdwmyke 711
bjmj 652
aawtvezfntstrcpgbzjbf -1000
aawtvezfntstrcpgbzjbf -171
bjmj -302
aawtvezfntstrcpgbzjbf 961
zhahpvqiptvksnbjkdvmknb 848
bjmj -735
"""
# expected_output = """aawtvezfntstrcpgbzjbf"""
# s = sys.stdin.read() # submit

lines: list = s.split("\n")  # dev
lines = lines[1:-1]
from collections import defaultdict

name_to_score_dict = defaultdict(int)
score_to_name_list_dict = defaultdict(list)
for line in lines:
    name, score = line.split()
    score = int(score)
    new_score = name_to_score_dict[name] + score
    old_score = name_to_score_dict[name]
    name_to_score_dict[name] = new_score
    # remove old score from score_to_name_list_dict
    if name in score_to_name_list_dict[old_score]:
        score_to_name_list_dict[old_score].remove(name)
    score_to_name_list_dict[new_score].append(name)
max_score = max(name_to_score_dict.values())
result = score_to_name_list_dict[max_score][0]
candidate = score_to_name_list_dict[max_score]
name_to_score_dict = defaultdict(int)
for line in lines:
    name, score = line.split()
    score = int(score)
    name_to_score_dict[name] += score
    if name_to_score_dict[name] >= max_score and name in candidate:
        result = name
        break
print(result)
