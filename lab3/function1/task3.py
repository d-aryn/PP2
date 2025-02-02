def solve(heads, legs):
    chicken = 0
    rabbit = 0
    for i in range(1, heads+1):
        if i*2+(heads-i)*4==legs:
            chicken = i
            rabbit = heads-i
            break
    
    if(chicken != 0 and rabbit != 0):
        return chicken, rabbit
    else:
        return "No solution"

heads = 35
legs = 94

res = solve(heads, legs)
if type(res)==tuple:
    print(f"There are {res[0]} rabbits and {res[1]} chickens")
else:
    print(res)

#Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):