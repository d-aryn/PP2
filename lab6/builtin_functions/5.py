def check_true(tup):
    return all(tup)

t1 = (1, 4, 6, True)
t2 = (0, 5, False)

print(check_true(t1))
print(check_true(t2))