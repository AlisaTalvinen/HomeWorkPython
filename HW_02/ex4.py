# 4)Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

n = int(input('Input an integer number: '))
sum = 0
for i in range(2, n + 1, 2):
    sum += i
print(f'The sum of even numbers located between the numbers 1 and {n} inclusive is {sum}')
