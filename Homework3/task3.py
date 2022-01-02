# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

ls = [random.randint(1, 100) for _ in range(20)]
print(ls)
min_el = 100
max_el = 0
for i in range(len(ls)):
    if ls[i] > max_el:
        max_el = ls[i]
    # print(max_el)
    if ls[i] < min_el:
        min_el = ls[i]
index_min=ls.index(min_el)
index_max=ls.index(max_el)
ls[index_min], ls[index_max] = ls[index_max], ls[index_min]
print(ls)
print(min_el, max_el)