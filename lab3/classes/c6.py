def isprime(x):
    if x<2:
        return False
    count = 0
    for i in range(1, x+1):
        if x%i==0:
            count+=1
    
    if count!=2:
        return False
    
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

arr = list(filter(lambda x: isprime(x), numbers))

print(arr)