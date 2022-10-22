exp_number = input('Введите число в экспоненциальной форме: ')
mantissa = exp_number.split('e')[0]
order = exp_number.split('e')[1]
print(f'Мантисса числа: {mantissa}')
print(f'Порядок числа: {order}')
