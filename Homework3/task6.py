# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
import random

ls = [random.randint(1, 100) for _ in range(20)]
print(ls)
max = 0
min = 100
sum = 0
for i in range(len(ls)):
    if ls[i] > max:
        max = ls[i]
        i += 1
    if ls[i] < min:
        min = ls[i]
        i += 1
min_ind = ls.index(min)
max_ind = ls.index(max)
if min_ind < max_ind:
    for i in range((min_ind + 1), max_ind):
        sum += ls[i]
else:
    for i in range((max_ind + 1), min_ind):
        sum += ls[i]
print(sum)