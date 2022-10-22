text = input('Введите текст: ')
vowels_list = [let for let in text if let in 'аиеёоуыэюя']
print(f'Список гласных букв: {vowels_list}')
print(f'Длина списка: {len(vowels_list)}')
