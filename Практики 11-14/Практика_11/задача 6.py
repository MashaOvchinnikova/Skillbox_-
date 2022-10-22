print('Ввод:')
lower_bound = int(input('Нижняя граница: '))
upper_bound = int(input('Верхняя граница: '))
step = int(input('Шаг: '))
print('Вывод:')
print('C F')

for degree in range(lower_bound, upper_bound + step, step):
    if degree > upper_bound:
        degree = upper_bound
    res = int(degree * 1.8 + 32)
    print(degree, res)
