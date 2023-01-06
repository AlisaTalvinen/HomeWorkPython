# 2) Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5


n = int(input('Input an integer number: '))
d = 2
while n % d != 0:
    d += 1
print (f'The smallest natural divisor of an integer {n} is {d}')
