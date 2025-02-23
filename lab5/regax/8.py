import re
pattern = r'(?=[A-Z])'
txt = 'NursadykDaryn'
a = re.split(pattern, txt)
print(a)