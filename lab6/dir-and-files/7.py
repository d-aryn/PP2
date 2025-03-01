with open('4.txt', 'r') as file1: 
    content1 = file1.read()
with open('5.txt', 'a') as file2:
    file2.write('\n')
    file2.write(content1)
