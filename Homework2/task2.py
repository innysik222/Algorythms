#2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)
def count_even(num):
	count_even=0
	count_uneven=0
	while num!=0:
		n=num%10
		num=num//10
		if n%2==0:
			count_even+=1
		else:
			count_uneven+=1
	return print(f"количество четных цифр -{count_even},  нечетных-{count_uneven}")
count_even(56784268)