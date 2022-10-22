import math

a = float(input('Введите действительный коэффициент a≠0: '))
b = float(input('Введите действительный коэффициент b: '))
c = float(input('Введите действительный коэффициент c: '))
discriminant = b**2 - 4 * a * c

if discriminant == 0:
    x = -b / (2 * a)
    print(x)
elif discriminant > 0:
    x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
    if x_1 > x_2:
        print(x_2, x_1)
    else:
        print(x_1, x_2)
