import re
pattern = r'_([a-z])'
txt = 'i_love_you'
camelcase = re.sub(pattern, lambda x: x.group(1).upper(), txt)
print(camelcase)