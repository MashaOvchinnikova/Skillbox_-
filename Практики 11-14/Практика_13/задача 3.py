def reversed_number(n):
    rev = 0
    while n > 0:
        last_digit = n % 10
        rev = rev * 10 + last_digit
        n //= 10
    return rev


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
summa = reversed_number(first_number) + reversed_number(second_number)
print(f'Первое число наоборот: {reversed_number(first_number)}')
print(f'Второе число наоборот: {reversed_number(second_number)}')
print(f'Сумма: {summa}')
print(f'Сумма наоборот: {reversed_number(summa)}')
