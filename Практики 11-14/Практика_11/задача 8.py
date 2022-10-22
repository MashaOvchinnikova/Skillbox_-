alpha = float(input('Введите угол поворота часовой стрелки: '))
minute_hand_angle = alpha * 12
print(f'C начала последнего часа минутная стрелка повернулась на {minute_hand_angle % 360} градусов')
