# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 
# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h
#     a, b, c, d, e, h - рандом


from random import randint

k = int(input('Введите степень K: '))
for i in range (k, 0 , -1):
    factor = randint(1, 100)
    if factor == 1:
        factor = ''
    else:
        if i != 1:
            factor = f'{factor}*x^{i} +'
        else:
            factor = f'{factor}*x +'
    print(factor, end=' ')

print(f'{randint(1, 101)} = 0')












