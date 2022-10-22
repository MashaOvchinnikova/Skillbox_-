films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
         'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorite_films = []
count = int(input('Сколько фильмов хотите добавить? '))

for film in range(count):
    film_name = input('Введите название фильма: ')
    if film_name in films:
        favorite_films.append(film_name)
    else:
        print(f'Ошибка: фильма {film_name} у нас нет :(')

print(f'Ваш список любимых фильмов: {", ".join(favorite_films)}')
