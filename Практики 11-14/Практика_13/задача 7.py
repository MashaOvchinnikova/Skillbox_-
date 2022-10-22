max_danger = float(input('Введите максимально допустимый уровень опасности: '))
d_from = 0
d_to = 4
depth = d_from + (d_to - d_from) // 2
danger = depth**3 - 3 * depth**2 - 12 * depth + 10

if max_danger < 0:
    print('Ошибка: максимально допустимый уровень опасности должен быть больше нуля')
else:
    print('Depth:', depth, 'Danger:', danger)
    while abs(danger) > max_danger:
        if danger > 0:
            d_from = depth
        else:
            d_to = depth
        depth = d_from + (d_to - d_from) // 2
        danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
        print('Depth:', depth, 'Danger:', danger)

print('Приблизительная глубина безопасной кладки:', depth, 'метров')
