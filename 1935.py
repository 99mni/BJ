N = int(input())
expr = input()
stack, val =[], []
for i in range(0,N):
	val.append(int(input()))

ll = len(expr)
for i in range(0,ll):
	n = expr[i]
	if  (ord(n) >= ord('A') and ord(n)<= ord('Z')):
		t = ord(expr[i]) - ord('A')
		stack.append(val[t])
	else:
		t2 = stack.pop()
		t1 = stack.pop()
		if (expr[i]=='+'):
			stack.append(t1+t2)
		elif (expr[i] =='-'):
			stack.append(t1-t2)
		if (expr[i]=='*'):
			stack.append(t1*t2)
		elif (expr[i] =='/'):
			stack.append(t1/t2)
print('{:.2f}'.format(stack.pop()))