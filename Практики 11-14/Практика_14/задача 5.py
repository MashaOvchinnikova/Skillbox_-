def smallest_divisor(n):
    divisor = 0
    for number in range(2, n + 1):
        if n % number == 0:
            divisor = number
            break
    return divisor


number = int(input('Введите число: '))
print(f'Наименьший делитель, отличный от единицы: {smallest_divisor(number)}')
