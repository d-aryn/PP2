import os
path = r'/Users/darynnursadyk/Desktop/screenshot'

print("Только директории:")
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)

print("\nТолько файлы:")
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        print(i)

print("\nВсе директории и файлы:")
for i in os.listdir(path):
    print(i)