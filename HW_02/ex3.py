# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]


n = int(input('Input an integer number: '))

listNum = []
for i in range(-n, n + 1):
    listNum.append(i)
print(listNum)

amount = 5
listInd = []
for i in range(amount):
    listInd.append(int(input(f'Input {i+1} index: ')))

product = 1
for i in listInd:
    product *= listNum[i]
    print(listNum[i], end=' ')
print(f'\n= {product}')
