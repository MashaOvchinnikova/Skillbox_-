def max_of_two_numbers(a, b):
    max_num = ((a + b) + abs(a - b))//2
    return max_num


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))
max_of_three_numbers = max_of_two_numbers((max_of_two_numbers(first_number, second_number)), third_number)
print(f'Максимальное число из трех: {max_of_three_numbers}')
