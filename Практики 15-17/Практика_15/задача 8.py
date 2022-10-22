def make_list():
    n = int(input('Введите длину списка: '))
    new_list = []
    for _ in range(n):
        number = int(input('Введите число: '))
        new_list.append(number)
    return new_list


lst = make_list()
shift = int(input('Сдвиг: '))
print(f'Изначальный список: {lst}')
for i in range(shift):
    lst.append(lst.pop(0))
print(f'Сдвинутый список: {lst}')
