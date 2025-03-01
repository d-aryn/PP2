import string

letters = string.ascii_uppercase

for letter in letters:
    filename = f"{letter}.txt"
    with open(filename, 'w') as file:
        pass