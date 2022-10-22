numbers = int(input('Введите число: '))
odd_num_list = []

for number in range(1, numbers + 1):
    if number % 2 != 0:
        odd_num_list.append(number)

print('Список из нечётных чисел от одного до N:', odd_num_list)
