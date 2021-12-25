#. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
max_sum=0
max_digit=0
n=int(input('введите число от 1 до 10000'))
while n!=0:
	m=n
	s=0
	while n>0:
		digit=n%10
		s+=digit
		n=n//10

	if s>max_sum:
		max_sum=s
		max_digit=m
	n = int(input('введите число от 1 до 10000'))
print(f'число {max_digit} имеет максимальную сумму цифр {max_sum}')