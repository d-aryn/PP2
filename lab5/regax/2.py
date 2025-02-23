import re
pattern = r'ab{2,3}'
txt = ['abb', 'aaabbb', 'ba']

for i in txt:
    if re.fullmatch(pattern, i):
        print(f"Строка '{i}' соответствует шаблону")
    else:
        print(f"Строка '{i}' не соответствует шаблону")

