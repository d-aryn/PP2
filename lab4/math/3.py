import math
sides = int(input())
length_side = float(input())
r = math.radians(180/sides)
A = length_side/(2 * math.tan(r))
S = (sides * length_side * A)/2
print(S)