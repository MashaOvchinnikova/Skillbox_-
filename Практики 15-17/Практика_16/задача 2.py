def sort_list(some_list):
    for i in range(len(some_list)):
        for cur_elem in range(i, len(some_list)):
            if some_list[i] > some_list[cur_elem]:
                some_list[cur_elem], some_list[i] = some_list[i], some_list[cur_elem]
    return some_list


first_class = list(range(160, 177, 2))
second_class = list(range(162, 181, 3))
first_class.extend(second_class)
print(f'Отсортированный список учеников: {sort_list(first_class)}')
