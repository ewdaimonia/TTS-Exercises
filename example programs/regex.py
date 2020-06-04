from sys import stdin
import re
p = re.compile(r'(?<= )&&(?= )', re.IGNORECASE)
g = re.compile(r'(?<= )\|\|(?= )', re.IGNORECASE)
lines = stdin.read().splitlines()
lines.pop(0)
for i in range(len(lines)):
    lines[i] = re.sub(p, "and", lines[i])
    lines[i] = re.sub(g, "or", lines[i])
for i in lines:
    print(i)
