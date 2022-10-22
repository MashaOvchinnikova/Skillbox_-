main_list = [1, 5, 3]
first_side_list = [1, 5, 1, 5]
second_side_list = [1, 3, 1, 5, 3, 3]
main_list.extend(first_side_list)
fives_count = main_list.count(5)
print(f'Кол-во цифр 5 при первом объединении: {fives_count}')

for _ in range(fives_count):
    main_list.remove(5)

main_list.extend(second_side_list)
triples_count = main_list.count(3)
print(f'Кол-во цифр 3 при втором объединении: {triples_count}')
print(f'Итоговый список: {main_list}')
