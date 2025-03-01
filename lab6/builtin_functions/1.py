from math import prod

s = []
n = int(input())
for i in range(n):
    r = int(input())
    s.append(r)

print(prod(s))