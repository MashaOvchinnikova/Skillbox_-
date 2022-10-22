word = input('Введите слово: ')
letters = list(word)
unique_letters = []

for letter in letters:
    if letters.count(letter) == 1:
        unique_letters.append(letter)

print(f'Количество уникальных букв: {len(unique_letters)}')
