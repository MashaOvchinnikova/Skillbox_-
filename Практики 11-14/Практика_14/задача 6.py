import math


def is_in_border(x, y, r):
    if math.sqrt(x ** 2 + y ** 2) <= r:
        return True


x = float(input('X: '))
y = float(input('Y: '))
r = int(input('Введите радиус: '))

if is_in_border(x, y, r):
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')
