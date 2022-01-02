# Определить, какое число в массиве встречается чаще всего.
import random

ls = [random.randint(1, 100) for _ in range(50)]
print(ls)
num = 0
min_frq = 1
for i in range(len(ls) - 1):
    count = 1
    for k in range(i + 1, len(ls)):
        if ls[i] == ls[k]:
            count += 1
    if count > min_frq:
        min_frq = count
        num = ls[i]
if min_frq > 1:
    print(f"число {num} встречается {min_frq} раз")
else:
    print("все числа уникальны")