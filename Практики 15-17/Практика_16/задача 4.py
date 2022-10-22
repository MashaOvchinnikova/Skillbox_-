guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'\nСейчас на вечеринке {len(guests)} человек: {guests}')
    user_response = input('Гость пришёл или ушёл? ')
    if user_response == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    guest_name = input('Имя гостя: ')
    if user_response == 'пришёл':
        if len(guests) < 6:
            print(f'Привет, {guest_name}!')
            guests.append(guest_name)
        else:
            print(f'Прости, {guest_name}, но мест нет')
    elif user_response == 'ушёл':
        print(f'Пока, {guest_name}!')
        guests.remove(guest_name)
    else:
        print('Ошибка ввода: введите "пришёл" или "ушёл"')
