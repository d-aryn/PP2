def has_33(nums):
    if(3 not in nums):
        return False
    
    ind = nums.index(3)
    count = nums.count(3)
    if(len(nums)-ind==count):
        return True
    
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 3, 3]))
print(has_33([3, 1, 3]))


#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.