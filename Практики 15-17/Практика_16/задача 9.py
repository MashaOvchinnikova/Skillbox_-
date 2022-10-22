friends_list = [0] * int(input('Кол-во друзей: '))
debt_receipts_number = int(input('Долговых расписок: '))

for dept in range(debt_receipts_number):
    print(f'\n{dept + 1}-я расписка:')
    whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    friends_list[whom - 1] -= how_much
    friends_list[from_whom - 1] += how_much

print('Баланс друзей:')

for index, value in enumerate(friends_list, start=1):
    print(f'{index}: {value}')
