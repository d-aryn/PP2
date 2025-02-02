arr = [1, 1, 1, 2, 2, 1, 1, 4, 4, 5, 6, 6, 6, 10, 10, 9, 9, 9]

def unique():
    global arr
    k = arr[0]
    newarr = []
    newarr.append(k)
    for i in range(1, len(arr)):
        if arr[i]!=k:
            k=arr[i]
            newarr.append(k)
    arr = newarr
    

    
unique()
print(arr)

#Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.