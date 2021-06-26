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