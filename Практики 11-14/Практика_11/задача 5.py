import math
radius = float(input('Введите радиус случайной планеты: '))
earth_volume = 10.8321 * 10**11
random_planet_volume = 4/3 * math.pi * radius**3
volume_ratio = round(earth_volume / random_planet_volume, 3)

if volume_ratio > 1:
    print(f'Объём планеты Земля больше в {volume_ratio} раз')
elif volume_ratio < 1:
    print(f'Объём планеты Земля меньше в (1/{volume_ratio})={round(1 / volume_ratio, 3)} раз')
else:
    print('Объемы планет равны')
