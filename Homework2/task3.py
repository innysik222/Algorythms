#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
def reverse_order(num):
	n2=0
	while num!=0:
		n=num%10
		num=num//10
		n2=n2*10
		n2=n2+n
	print(n2)
reverse_order(8765479)