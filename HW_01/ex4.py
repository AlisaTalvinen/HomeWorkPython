# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def showQuart(quartNum):
    if quartNum >= 1 and quartNum <= 4:
        if (quartNum == 1): print('x > 0 and y > 0')
        elif (quartNum == 2): print('x < 0 and y > 0')
        elif (quartNum == 3): print('x < 0 and y < 0')
        else: print('x > 0 and y < 0')
    else:
        print('Введено неверное число')

num = int(input('Введите номер четверти: '))
showQuart(num)











