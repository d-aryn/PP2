def primes(arr):
    
    for i in arr:
        if i == 1:
            continue
        count = 0
        for j in range(1, i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
primes(arr)

#You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

