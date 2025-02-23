import re
pattern = r'^a.+b$'
txt = ['akjfb', 'bd', 'aabb', 'akdb']

for i in txt:
    if re.fullmatch(pattern, i):
        print(f"Строка '{i}' соответствует шаблону")
    else:
        print(f"Строка '{i}' не соответствует шаблону")