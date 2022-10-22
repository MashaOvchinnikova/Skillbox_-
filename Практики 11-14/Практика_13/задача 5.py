def numbers_count(number):
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count


def modified_number(number):
    last_digit = number % 10
    first_digit = number // 10 ** (numbers_count(number) - 1)
    between_digits = number % 10 ** (numbers_count(number) - 1) // 10
    return last_digit * 10 ** (numbers_count(number) - 1) + between_digits * 10 + first_digit


first_n = int(input("Введите первое число: "))
second_n = int(input("\nВведите второе число: "))

if numbers_count(first_n) < 3:
    print("В первом числе меньше трёх цифр.")
elif numbers_count(second_n) < 4:
    print("Во втором числе меньше четырёх цифр.")
else:
    print(f'Изменённое первое число: {modified_number(first_n)}')
    print(f'Изменённое второе число: {modified_number(second_n)}')
    print('\nСумма чисел:', {modified_number(first_n) + modified_number(second_n)})
