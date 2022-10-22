import random

before_compression = [random.randint(0, 2) for _ in range(int(input('Количество чисел в списке: ')))]
print(f'Список до сжатия: {before_compression}')

for el in before_compression:
    if el == 0:
        before_compression.append(el)
        before_compression.remove(el)

after_compression = before_compression[:len(before_compression) - before_compression.count(0)]
print(f'Список после сжатия: {after_compression}')
