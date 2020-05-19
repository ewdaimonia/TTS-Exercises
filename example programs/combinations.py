from itertools import combinations_with_replacement
gotten = input().split(" ")
sorted(gotten[0])
combinations = list(
    map("".join, combinations_with_replacement(gotten[0], int(gotten[1]))))
combinations = list(
    map(lambda i: i[::-1] if (i[0] > i[1]) else i, combinations))
combinations.sort()
for i in combinations:
    print(i)
