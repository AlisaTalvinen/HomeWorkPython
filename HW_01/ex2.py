# 2. (!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print(x, y, z, ': ', (not (x or y or z)) == (not x and not y and not z))
