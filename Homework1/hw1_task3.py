#Написать программу, которая генерирует в указанных пользователем границах:
#a. случайное целое число,
#b. случайное вещественное число,
#c. случайный символ.
#Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random
print("введите два целых числа, ограничивающих интервал целых чисел")
x=int(input('введите первое число '))
y=int(input('введите второе число '))
if x<y:
  print(f"случайное число из заданного интервала-{random.randint(x,y)}")
else:
  print(f"случайное число из заданного интервала-{random.randint(y,x)}")

print("введите два вещественных числа, ограничивающих интервал вещественных чисел")
x = float(input('введите первое число '))
y = float(input('введите второе число '))
if x < y:
  print(f"случайное число из заданного интервала-{random.uniform(x, y)}")
else:
  print(f"случайное число из заданного интервала-{random.uniform(y, x)}")

print("введите два символа от a до z")
x = input('введите первый символ ')
y = input('введите второй символ ')
if ord(x)<ord(y):
  print(f"случайный символ из заданного интервала-{chr(random.randint(ord(x),ord(y)))}")
else:
  print(f"случайный символ из заданного интервала-{chr(random.randint(ord(y),ord(x)))}")
