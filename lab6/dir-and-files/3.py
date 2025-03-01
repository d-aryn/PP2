import os

path = '/Users/darynnursadyk/Documents/hw'

if os.path.exists(path):
    print('существует')

    directory, filename = os.path.split(path)
    print('filename = ', filename)
    print('directory = ', directory)
else:
    print('не существует')