people_list = list(range(1, int(input('Кол-во человек: ')) + 1))
number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number}-й человек')

out = 0
count_start = 0
while len(people_list) > 1:
    print(f'\nТекущий круг людей: {people_list}')
    print(f'Начало счёта с номера {people_list[count_start]}')
    out = people_list[(count_start + number - 1) % len(people_list)]
    print(f'Выбывает человек под номером {out}')
    count_start = people_list.index(out)
    if count_start == len(people_list) - 1:
        count_start = 0
    people_list.remove(out)

print(f'\nОстался человек под номером {people_list[0]}')
