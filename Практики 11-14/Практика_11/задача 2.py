import math
n = int(input('Введите кол-во чисел: '))

for number in range(n):
    x = float(input('Введите число: '))
    if x == 0:
        continue
    if x > 0:
        x = math.ceil(x)
        print(f'x={x} log(x)={math.log(x)}')
    else:
        x = math.floor(x)
        print(f'x={x} exp(x)={math.exp(x)}')
