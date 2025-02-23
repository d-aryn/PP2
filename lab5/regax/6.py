import re
pattern = r'[ ,.]'
txt = ['hello, world', 'a.l.ma ty']

for i in txt:
    print(re.sub(pattern, ':', i))