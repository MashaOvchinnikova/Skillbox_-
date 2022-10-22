number = float(input('Введите число: '))
b = 0
if number >= 1:
    while number >= 10:
        number /= 10
        b += 1
    print(number, '*', '10**', b, sep='')
elif 0 < number < 1:
    while number < 1:
        number *= 10
        b -= 1
    print(round(number, 2), '*', '10**', b, sep='')
else:
    print('Ошибка ввода')

