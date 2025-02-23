import re
pattern = r'[A-Z][a-z]+'
txt = ['Alkj', 'kjdf', 'VVkfk', 'Njfjl']

for i in txt:
    if re.fullmatch(pattern, i):
        print(f"Строка '{i}' соответствует шаблону")
    else:
        print(f"Строка '{i}' не соответствует шаблону")