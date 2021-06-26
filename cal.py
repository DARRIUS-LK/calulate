x = input('please input the first no. : ')
y = input('please input the second no.: ')
op = input('what operation would u like (+, -, *, /) :')
if op == '+':
	ans = float(x)+float(y)
	print('the answer is: ', ans)
elif op == '-':
	ans = float(x)-float(y)
	print('the answer is: ', ans)
elif op == '*':
	ans = float(x)*float(y)
	print('the answer is: ', ans)
elif op == '/':
	ans = float(x)/float(y)
	print('the answer is: ', ans)
b = ans
z = input('do u want to continue calculating with the answer (yes/no): ')
if z == 'yes':
	w = input('please input the no. : ')
	op2 = input('what operation would u like (+, -, *, /) :')
	if op2 == '+':
		c = b+float(w)
		print('the answer is: ', c)
	elif op2 == '-':
		c = b-float(w)
		print('the answer is: ', c)
	elif op2 == '*':
		c = b*float(w)
		print('the answer is: ', c)
	elif op2 == '/':
		c = b/float(w)
		print('the answer is: ', c)
if z == 'no':
	print('thankyou.')
