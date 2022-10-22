print('Введите местоположение коня:')
horse_x = float(input())
horse_y = float(input())
print('Введите местоположение точки на доске:')
x = float(input())
y = float(input())

horse_x_square = int(horse_x * 10)
horse_y_square = int(horse_y * 10)
x_square = int(x * 10)
y_square = int(y * 10)
print(f'Конь в клетке ({horse_x_square}, {horse_y_square}). Точка в клетке ({x_square}, {y_square}).')

dx = abs(horse_x_square - x_square)
dy = abs(horse_y_square - y_square)
if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print('Да, конь может ходить в эту точку.')
else:
    print('Конь не может ходить в эту точку')
