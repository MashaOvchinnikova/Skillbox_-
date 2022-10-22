def reversed_number(n):
    string = str(n).split('.')
    rev = string[0][::-1] + '.' + string[1][::-1]
    return float(rev)


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
summa = reversed_number(first_number) + reversed_number(second_number)
print(f'Первое число наоборот: {reversed_number(first_number)}')
print(f'Второе число наоборот: {reversed_number(second_number)}')
print(f'Сумма: {summa}')
