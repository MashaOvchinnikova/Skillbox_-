def reversed_number(n):
    rev = 0
    while n > 0:
        last_digit = n % 10
        rev = rev * 10 + last_digit
        n //= 10
    return rev


while True:
    number = int(input('Введите число: '))
    if number == 0:
        break
    print(f'Число наоборот: {reversed_number(number)}\n')

print('Программа завершена!')
