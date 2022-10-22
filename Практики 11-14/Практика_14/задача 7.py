def is_three_identical_digits(number):
    digits = []

    while number != 0:
        digits.append(number % 10)
        number //= 10

    for index, value in enumerate(digits):
        if digits.count(value) == 3:
            return True


first_year = int(input('Введите первый год: '))
last_year = int(input('Введите второй год: '))
print(f'Годы от {first_year} до {last_year} с тремя одинаковыми цифрами:')

for year in range(first_year, last_year + 1):
    if is_three_identical_digits(year):
        print(year)
