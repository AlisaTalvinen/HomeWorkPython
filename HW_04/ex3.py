# Задайте последовательность чисел. Напишите программу, которая выведет список элементов, которые не имели повторов в исходной последовательности.
# Ввод: 3 1 2 3
# Вывод: 2 1


nums = [int(i) for i in input('Введите числа через пробел: ').split()]
list = []
for i in nums:
    if nums.count(i) == 1:
        list.append(i)
print('Данные числа встречаются один раз:')
print(*list)
