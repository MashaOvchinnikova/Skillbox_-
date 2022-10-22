initial_amplitude = float(input('Введите начальную амплитуду: '))
stopping_amplitude = float(input('Введите амплитуду остановки: '))

if initial_amplitude <= stopping_amplitude:
    print('Ошибка ввода: начальная амплитуда должна быть больше амплитуды остановки')
else:
    count = 0
    percent = 8.4 / 100
    while initial_amplitude > stopping_amplitude:
        initial_amplitude *= 1 - percent
        count += 1
    print(f'Маятник считается остановившимся через {count} колебаний')
