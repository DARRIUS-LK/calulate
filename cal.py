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
else:
	print('thankyou.')
answer_stored = ans
further_continue  = input('do u want to continue calculating with the answer (yes/no): ')
if further_continue == 'yes':
	z = input('please input the next no. : ')
	op2 = input('what operation would u like (+, -, *, /) :')
	if op2 == '+':
		ans2 = answer_stored+float(z)
		print('the answer is: ', ans2)
	elif op2 == '-':
		ans2 = answer_stored-float(z)
		print('the answer is: ', ans2)
	elif op2 == '*':
		ans2 = answer_stored*float(z)
		print('the answer is: ', ans2)
	elif op2 == '/':
		ans2 = answer_stored/float(z)
		print('the answer is: ', ans2)
else:
	print('thankyou.')
