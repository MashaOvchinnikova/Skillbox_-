containers_number = int(input('Количество контейнеров: '))
weights_list = []

for container in range(containers_number):
    weight = int(input('Введите вес контейнера: '))
    if weight > 200:
        print('Ошибка ввода: вес контейнера не должен превышать 200 кг')
    else:
        weights_list.append(weight)

new_container = int(input('Введите вес нового контейнера: '))

prev_value = 0
for index, value in enumerate(weights_list, start=1):
    if value < new_container <= prev_value:
        print(f'Номер, который получит новый контейнер: {index}')
    prev_value = value
