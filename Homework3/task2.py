# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
import random

ls = [random.randint(1, 100) for _ in range(100)]
index_ls = []
print(ls)
count = 0
for i in range(len(ls)):
    if ls[i] % 2 == 0:
        count += 1
        index_ls.append(i)
print(index_ls)
print(count)
print(len(index_ls))


















