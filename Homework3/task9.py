# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

M = 4
N = 3
matrix = [[random.randint(1, 20) for _ in range(N)] for _ in range(M)]
for item in matrix:
    print(item)
max = 0
for j in range(N):
    min = 20
    for i in range(M):
        if matrix[i][j] < min:
            min = matrix[i][j]
    if min > max:
        max = min

print("Максимальный среди минимальных: ", max)