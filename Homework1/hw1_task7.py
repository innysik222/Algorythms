# Определить, является ли год, который ввел пользователь, високосным или не високосным.
x=int(input("Введите значение года"))
if x%4==0:
	if x%100==0:
		if x%400==0:
			print("это високосный год")
	else:
	  print("это високосный гoд")
else:
	print("Год не високосный")










