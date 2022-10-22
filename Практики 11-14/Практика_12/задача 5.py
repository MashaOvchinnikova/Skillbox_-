def count_letters(text, number, letter):
    numbers_count = 0
    letters_count = 0

    for symbol in text:
        if symbol == str(number):
            numbers_count += 1
        elif symbol == letter:
            letters_count += 1

    print(f'Количество цифр {number}: {numbers_count}')
    print(f'Количество букв {letter}: {letters_count}')


text = input('Введите текст: ')
number = int(input('Какую цифру ищем? '))
letter = input('Какую букву ищем? ')
count_letters(text, number, letter)
