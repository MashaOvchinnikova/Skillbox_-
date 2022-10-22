def make_list(length, list_number):
    new_list = []
    for i_number in range(length):
        element = int(input(f'Введите {i_number + 1}-е число для {list_number}-го списка: '))
        new_list.append(element)
    return new_list


first_list = make_list(3, 1)
second_list = make_list(7, 2)
print(f'Первый список: {first_list}')
print(f'Второй список: {second_list}')
first_list.extend(second_list)

for number in first_list:
    if first_list.count(number) > 1:
        for duplicate in range(first_list.count(number) - 1):
            first_list.remove(number)

print(f'Новый первый список с уникальными элементами: {first_list}')
