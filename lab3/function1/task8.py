def spy_game(nums):
    seq = [0, 0, 7]
    for i in nums:
        if i == seq[0]:
            seq.pop(0)
        if not seq:
            return True
        
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,0,7]))
print(spy_game([1,7,2,0,4,5,0]))