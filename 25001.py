ss = input()
stack, fr, re = [], [], []
rdic ={'(':')', '[':']', '{':'}'}
dic ={')':'(', ']':'[', '}':'{'}
ans = True
for i in range(len(ss)):
	if (ss[i] ==']' or ss[i] =='}' or ss[i] ==')'):
		if (len(stack)==0):
			fr.append( dic[ss[i]] )
		else:
			if (dic[ss[i]] != stack[-1]):
				ans = False
				break
			else:
				stack.pop()
	else:
		stack.append(ss[i])
fr.reverse()
ll = len(stack)
for i in range(ll-1, -1, -1):
	re.append(rdic[stack[i]])
if (ans == True):
	print(''.join(fr)+ ss+ ''.join(re))
else:
	print('NIE')