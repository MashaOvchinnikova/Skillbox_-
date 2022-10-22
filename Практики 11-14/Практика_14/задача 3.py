def digits_sum(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s


def digits_count(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count


number = int(input('Введите число: '))
diff = digits_sum(number) - digits_count(number)
print(f'Сумма цифр: {digits_sum(number)}')
print(f'Количество цифр в числе: {digits_count(number)}')
print(f'Разность суммы и количества цифр: {diff}')
