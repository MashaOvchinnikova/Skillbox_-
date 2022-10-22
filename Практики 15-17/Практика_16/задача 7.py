def make_skates_list():
    skates_list = []
    skates_number = int(input('\nКол-во коньков: '))
    for number in range(skates_number):
        skate_size = int(input(f'Размер {number + 1}-й пары: '))
        skates_list.append(skate_size)
    return skates_list


def make_people_list():
    people_list = []
    people_number = int(input('\nКол-во людей: '))
    for person in range(people_number):
        foot_size = int(input(f'Размер ноги {person + 1}-го человека: '))
        people_list.append(foot_size)
    return people_list


skates = make_skates_list()
people = make_people_list()
count = 0

for foot_size in people:
    for skate_size in skates:
        if foot_size <= skate_size:
            count += 1
            skates.remove(skate_size)
            break

print(f'Наибольшее кол-во людей, которые могут взять ролики: {count}')




