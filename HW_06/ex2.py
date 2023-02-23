# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]


data = [1, 'wasd', 3, 'ijk', 77]
print(data)
res_i = list(filter(lambda x: type(x) == int, data))
res_s = list(filter(lambda x: type(x) == str, data))
print(f'числа: {res_i}')
print(f'буквы: {res_s}')
