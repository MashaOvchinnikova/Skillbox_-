names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day = []
second_day = []

for i in range(len(names)):
    if i % 2 == 0:
        first_day.append(names[i])
    else:
        second_day. append(names[i])

print('Первый день:', first_day)
print('Второй день:', second_day)
