import time
import math

def root(number, milsec):
    time.sleep(milsec/1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {milsec} is {result}") 

a, b = int(input()), int(input())

root(a, b)