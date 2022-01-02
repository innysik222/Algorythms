# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу
matrix = []
for i in range(5):
    line = []
    sum = 0
    print(f"строка {i + 1}")
    for j in range(3):
        n = int(input("введите число"))
        sum += n
        line.append(n)
    line.append(sum)
    matrix.append(line)

for item in matrix:
    print(item)
print()