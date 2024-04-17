import sys
 
# s = """3
# 1 1 0
# 1 1 1
# 1 0 0
# """

s = sys.stdin.read()
lines = s.split("\n")
 
count = 0
for line in lines[1:-1]:
    a, b, c = map(int, line.split())
    if sum([a,b,c])>=2:
        count+=1
        
print(count)