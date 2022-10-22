def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


def my_func():
    number = int(input('Введите число: '))
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        print('Ошибка ввода. Введите число, отличное от нуля')


my_func()
