# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
n = int(input("введите количество чисел в последовательности "))
num = int(input("введите цифру, которую нужно подсчитать "))
import random

count = 0
count2 = 0
while count <= n:
    a = random.randint(1, 1000)
    count += 1
    print(a)
    if str(num) in str(a):
        count2 += 1
print(f"в выведенной последовательности {num} встречается {count2} раз")



