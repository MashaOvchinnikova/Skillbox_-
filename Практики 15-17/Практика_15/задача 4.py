video_cards_number = int(input('Количество видеокарт: '))
old_list = []
new_list = []


for video_card in range(video_cards_number):
    old_list.append(int(input(f'{video_card + 1} Видеокарта: ')))

max_value = max(old_list)

for i in range(len(old_list)):
    if old_list[i] < max_value:
        new_list.append(old_list[i])

print(old_list)
print(new_list)
