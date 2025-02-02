word = input() #for example "qazaq"
def check(word):
    if word == word[::-1]:
        return True
    
    return False

print(check(word))