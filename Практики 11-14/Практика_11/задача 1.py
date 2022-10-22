price = float(input('Введите стоимость покупки в евро: '))
price_in_rubles = round((price * 1.25) * 60.87, 2)
print(f'Стоимость покупки в рублях: {price_in_rubles}')
