import sys

s = """7 15
15 5 3 7 9 14 0
"""
s = """2 5
2 5
"""
# s = """46 615683844
# 431749087 271781274 274974690 324606253 480870261 401650581 13285442 478090364 266585394 425024433 588791449 492057200 391293435 563090494 317950 173675329 473068378 356306865 311731938 192959832 321180686 141984626 578985584 512026637 175885185 590844074 47103801 212211134 330150 509886963 565955809 315640375 612907074 500474373 524310737 568681652 315339618 478782781 518873818 271322031 74600969 539099112 85129347 222068995 106014720 77282307
# """
s = sys.stdin.read() # submit

lines: list = s.split("\n")  # dev

n, lenght = list(map(int, lines[0].split()))
lanterns = list(map(int, lines[1].split()))
lanterns = sorted(lanterns)
min_l = min(lanterns)
max_l = max(lanterns)
left = -min_l
right = lenght + (lenght - max_l)

left_pointer = [left] + lanterns
right_pointer = lanterns + [right]
d = 0
for l, r in zip(left_pointer, right_pointer):
    d = max(d, r - l)
print(d / 2)
