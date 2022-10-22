def find_coin(x, y):
    if (-1 <= x <= 1) and (-1 <= y <= 1):
        print('Монетка где-то рядом')
    else:
        print('Монетки рядом нет')


x = float(input('Введите значение x: '))
y = float(input('Введите значение y: '))
find_coin(x, y)
