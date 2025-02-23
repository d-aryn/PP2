import re

pat = r"ab*"

txt = ["abb", "aba", "bavb", "aaaab"]

for i in txt:
    if re.fullmatch(pat, i):
        print(f"Строка '{i}' соответствует шаблону")
    else:
        print(f"Строка '{i}' не соответствует шаблону")

