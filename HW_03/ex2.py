# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from random import randint
num = int(input('Введите размер списка: '))
list = []
new_list = []

for i in range(num):
    list.append(randint(0, 9))
print(list)

i = 0
while i < len(list)/2:
    num -= 1
    p = list[i] * list[num]
    new_list.append(p)
    i += 1

print(new_list)

