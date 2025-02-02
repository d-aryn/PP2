def generate_permutations(s, current=""):
    if len(s) == 0:  
        print(current)
    else:
        for i in range(len(s)):
            
            generate_permutations(s[:i] + s[i+1:], current + s[i])


string = "abcd"
generate_permutations(string)