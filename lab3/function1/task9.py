import math
def volume(rad):
    return (math.pi * math.pow(rad, 3) * 4)/3

radius = 42
vol = volume(radius)

print(f"The volume = {vol}")