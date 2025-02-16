def squares(N):
    for i in range(N+1):
        yield i**2
N = 5
for x in squares(N):
    print(x)
    