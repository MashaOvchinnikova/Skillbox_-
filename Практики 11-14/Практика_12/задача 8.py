# Нахождение НОД по алгоритму Евклида
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
print(f'НОД для чисел {first_number} и {second_number} равен {get_nod(first_number, second_number)}')
