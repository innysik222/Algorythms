# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.
import random

n = random.randint(0, 100)
count = 1
while count <= 10:
    num = int(input("угадайте целое число"))
    if num > n:
        print("введенное число больше загаданного")
    elif num < n:
        print("введенное число меньше загаданного")
    else:
        print("вы угадали!")
        break
    count += 1
print(f'загаданное число {n}')




