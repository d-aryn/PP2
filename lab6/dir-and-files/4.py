filename = '4.txt'
lines = 0
with open(filename) as file_object:
    for line in file_object:
        lines+=1
    print(lines)