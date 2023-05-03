import sys
input = sys.stdin.readline
dic ={')':'(', '}':'{', ']':'['}
left =set(['(', '{', '['])
def Check(ll) :
	n = len(ll)
	stack=[]
	for i in range(n):
		if ((ll[i] in left) == True):
			stack.append(ll[i])
		elif ((ll[i] in dic)== True):
			if (len(stack)==0):
				return "Illegal"
			if (stack[-1] != dic[ll[i]]):
				return "Illegal"
			stack.pop()
	if (len(stack)==0):
		return "Legal"
	else:
		return "Illegal"
R = []
while True:
	line = input()
	if (line[0]=='#'):
		break
	R.append(Check(line))

print('\n'.join(R))
