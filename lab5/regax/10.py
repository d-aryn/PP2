import re
pattern = r'([a-z])([A-Z])'
txt = 'CamelCaseString'

result = re.sub(pattern, r'\1_\2', txt).lower()
print(result)