def iter(n):
    while n >=0:
        yield n
        n = n - 1
n = int(input())
for x in iter(n):
    print(x)