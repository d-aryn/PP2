import re
pattern = r'([a-z])([A-Z])'

txt = 'KazakhBritishTechnicalUniversity'

result = re.sub(pattern, r'\1 \2', txt)
print(result)

#r'\1 \2': Используется для замены между первой и второй группой вставляется пробел.