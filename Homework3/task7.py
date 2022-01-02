# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба минимальны), так и различаться.
import random

ls = [random.randint(1, 100) for _ in range(20)]
print(ls)
min = 100
min2 = 100
for i in range(len(ls)):
    if ls[i] < min:
        min = ls[i]
        i += 1
ls.remove(min)
for i in range(len(ls)):
    if ls[i] < min2:
        min2 = ls[i]
        i += 1
print(f"минимальные элементы массива:{min, min2}")