def sort_list(some_list):
    for i in range(len(some_list)):
        for cur_elem in range(i, len(some_list)):
            if some_list[i] > some_list[cur_elem]:
                some_list[cur_elem], some_list[i] = some_list[i], some_list[cur_elem]
    return some_list


def make_list():
    n = int(input('Введите длину списка: '))
    new_list = []
    for _ in range(n):
        number = int(input('Введите число: '))
        new_list.append(number)
    return new_list


unsorted_list = make_list()
print(f'Изначальный список: {unsorted_list}')
print(f'Отсортированный список: {sort_list(unsorted_list)}')
