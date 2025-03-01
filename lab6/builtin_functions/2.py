lower = 0
upper = 0
r = input()
for char in r:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print("lower case letters = ", lower)
print("upper case letters = ", upper)

