import math
n_1=int(input('Введите первое число ='))
n_2=int(input('Введите второе число ='))
result=0
try:
    result=math.sqrt(n_1*n_2),
    print(f'Ответ:={result}')
except ValueError:
    print('Невозможно определить среднее геометрическое')