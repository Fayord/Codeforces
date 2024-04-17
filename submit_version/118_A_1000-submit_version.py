import sys

s = """Codeforces
"""
s = sys.stdin.read() # submit
lines: list = s.split("\n")  # dev
first_line = lines[0]
vowels = "AEIOUYaeiouy"
# alphabet a to z
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""
for letter in first_line:
    if letter in vowels:
        continue
    if letter.lower() in alphabet:
        result += "." + letter.lower()
print(result)
