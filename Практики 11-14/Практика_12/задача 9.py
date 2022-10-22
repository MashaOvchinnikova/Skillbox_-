import random


def rock_paper_scissors():
    # Игра "Камень, ножницы, бумага"
    user_choice = input('\nВыберите - камень, ножницы или бумага: ').lower()
    computer_choice = random.choice(['камень', 'ножницы', 'бумага'])
    if user_choice != 'камень' and user_choice != 'ножницы' and user_choice != 'бумага':
        print('Ошибка ввода: нужно ввести или "камень", или "ножницы", или "бумага"')
    else:
        print(f'Компьютер выбрал {computer_choice}')
        if user_choice == computer_choice:
            print('Ничья!')
        elif user_choice == 'камень':
            if computer_choice == 'ножницы':
                print('Камень бьёт ножницы. Вы победили!')
            else:
                print('Бумага кроет камень. Вы проиграли!')
        elif user_choice == 'ножницы':
            if computer_choice == 'бумага':
                print('Ножницы режут бумагу. Вы победили!')
            else:
                print('Камень бьёт ножницы. Вы проиграли!')
        else:
            if computer_choice == 'камень':
                print('Бумага кроет камень. Вы победили!')
            else:
                print('Ножницы режут бумагу. Вы проиграли!')

    play_again = int(input('Сыграем еще раз? (1 - да, 0 - нет)  '))
    if play_again == 0:
        input('Нажмите Enter, чтобы вернуться в меню')
        main_menu()
    elif play_again == 1:
        rock_paper_scissors()
    else:
        print('Ошибка ввода')
        main_menu()


def guess_the_number():
    # Игра "Угадай число"
    hidden_number = random.randint(0, 10)
    while True:
        number = int(input('\nВведите число (от 0 до 10): '))
        if number < 0 or number > 10:
            print('Ошибка ввода: нужно ввести число от 0 до 10')
        else:
            if number > hidden_number:
                print('Число больше, чем нужно. Попробуйте ещё раз!')
            elif number < hidden_number:
                print('Число меньше, чем нужно. Попробуйте ещё раз!')
            else:
                print('Вы угадали!')
                break

    play_again = int(input('Сыграем еще раз? (1 - да, 0 - нет)  '))
    if play_again == 0:
        input('Нажмите Enter, чтобы вернуться в меню')
        main_menu()
    elif play_again == 1:
        guess_the_number()
    else:
        print('Ошибка ввода')
        main_menu()


def main_menu():
    # Главное меню игры
    print('\n1. Игра "Камень, ножницы, бумага"', '2. Игра "Угадай число"', sep='\n')
    choice = int(input('В какую игру вы хотите сыграть? '))
    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        guess_the_number()
    else:
        print('Ошибка ввода: нужно ввести 1 или 2')
        main_menu()


main_menu()

