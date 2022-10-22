alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
char_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in message]
encrypted_message = ''

for char in char_list:
    encrypted_message += char

print(f'Зашифрованное сообщение: {encrypted_message}')
