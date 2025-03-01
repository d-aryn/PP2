filename = '5.txt'
item = ['naruto', 'boruto', 'Sakamoto days']
with open(filename, 'w') as file:
    for i in item:
        file.write(f"{i}\n")

        
with open(filename, 'r') as file:
    print(file.read())