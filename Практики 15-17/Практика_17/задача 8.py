sticks_condition = ['|' for condition in range(int(input('Количество палок: ')))]
K = int(input('Количество бросков: '))

for i in range(K):
    left = int(input(f'Бросок {i + 1}. Сбиты палки с номера '))
    right = int(input('по номер '))
    sticks_condition[left - 1: right] = '.' * (right - left + 1)

print(f'Результат: {"".join(sticks_condition)}')

