import math
size = float(input('Укажите размер файла для скачивания: '))
speed = float(input('Какова скорость вашего соединения? '))
time = int(size / speed)

for sec in range(1, time + 1):
    downloaded = speed * sec
    percent = int(round(downloaded / size, 2) * 100)
    print(f'Прошло {sec} сек. Скачано {downloaded} из {size} Мб ({percent}%)')
else:
    print(f'Прошло {math.ceil(size / speed)} сек. Скачано {size} из {size} Мб (100%)')
