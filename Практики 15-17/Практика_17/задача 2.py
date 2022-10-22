len_list = int(input('Введите длину списка: '))
result = [(1 if i_index % 2 == 0 else i_index % 5) for i_index in range(len_list)]
print(result)
