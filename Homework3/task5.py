# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

ls = [random.randint(-10, 10) for _ in range(20)]
print(ls)
max = -10
ls2 = []
for i in range(len(ls)):
    if ls[i] < 0:
        ls2.append(ls[i])
for i in range(len(ls2)):
    if ls2[i] > max:
        max = ls2[i]
        i += 1
print(f"максимальное отрицательное число: {max}")