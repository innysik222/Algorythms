#4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
n=int(input("Введите число элеметов ряда"))
sum=0
for i in range(0,n):
	num=1*((-0.5)**i)
	sum+=num
print(sum)