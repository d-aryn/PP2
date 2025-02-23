import re
pattern = r'[a-z]+_[a-z]+'
txt = ['abc_def', 'abc_mno_xyz', 'def_gh']
for i in txt:
    if re.fullmatch(pattern, i):
        print(f"Строка '{i}' соответствует шаблону")
    else:
        print(f"Строка '{i}' не соответствует шаблону")
