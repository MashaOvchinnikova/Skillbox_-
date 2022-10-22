def digits_sum(n):
    summa = 0
    while n > 0:
        summa += n % 10
        n //= 10
    print(f'Сумма цифр числа равна {summa}')


def max_digit(n):
    mx_digit = 0
    while n > 0:
        if n % 10 > mx_digit:
            mx_digit = n % 10
        n //= 10
    print(f'Максимальная цифра в числе - {mx_digit}')


def min_digit(n):
    mn_digit = 10
    while n > 0:
        if n % 10 < mn_digit:
            mn_digit = n % 10
        n //= 10
    print(f'Минимальная цифра в числе - {mn_digit}')


number = int(input('Введите число: '))

while True:
    action = int(input('Выберите действие: 1 - вывести сумму цифр числа, 2 - вывести максимальную цифру, '
                       '3 - вывести минимальную цифру\n'))
    if action == 1:
        digits_sum(number)
    elif action == 2:
        max_digit(number)
    elif action == 3:
        min_digit(number)
    else:
        break
