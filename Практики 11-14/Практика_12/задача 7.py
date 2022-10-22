def min_number(a, b):
    min_n = (a + b - abs(a - b)) // 2
    return min_n


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
print(f'Минимальное число равно {min_number(first_number, second_number)}')
