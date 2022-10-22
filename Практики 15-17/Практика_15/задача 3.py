cell_count = int(input('Количество клеток: '))
unsuitable_values = []

for cel in range(cell_count):
    effectiveness = int(input(f'Эффективность {cel + 1} клетки: '))
    if effectiveness < cel:
        unsuitable_values.append(effectiveness)

print('Неподходящие значения:', *unsuitable_values)
