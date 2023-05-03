def IsAlpha(n):
	if (n >='A' and n <='Z'):
		return True
	else:
		return False

icp = {'+':1, '-':1, '*':2, '/':2, '(':7}
isp = {'+':1, '-':1, '*':2, '/':2, '(':0}

expr = input()
stack, post, ll =[],[], len(expr)
for i in range(0,ll):
	if (IsAlpha(expr[i])==True):
		post.append(expr[i])
	elif (expr[i] ==')'):
		while(stack and stack[-1] != '('):
			post.append(stack[-1])
			stack.pop()
		stack.pop()
	else:
		while(stack and isp[stack[-1]]>= icp[expr[i]]):
			post.append(stack[-1])
			stack.pop()
		stack.append(expr[i])
while(stack):
	post.append(stack[-1])
	stack.pop()
print(''.join(post))