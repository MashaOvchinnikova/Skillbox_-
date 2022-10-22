import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
tour_winners = [(first_team[i_winner] if first_team[i_winner] > second_team[i_winner]
                 else second_team[i_winner]) for i_winner in range(20)]

print(f'Первая команда: {first_team}')
print(f'Вторая команда: {second_team}')
print(f'Победители тура: {tour_winners}')
