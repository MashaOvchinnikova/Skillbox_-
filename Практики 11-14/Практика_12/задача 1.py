def summa_n(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


number = int(input('Введите число: '))
print(f'Я знаю, что сумма чисел от 1 до {number} равна {summa_n(number)} ')



