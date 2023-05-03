import sys
s=sys.stdin.readline().strip()
res = 0
stack=[]

for i in s:
    if i == "+":
        a=stack.pop()
        b=stack.pop()
        stack.append(a+b)
    elif i=="-":
        a=stack.pop()
        b=stack.pop()
        stack.append(b-a)
    elif i=="*":
        a=stack.pop()
        b=stack.pop()
        stack.append(a*b)
    elif i=="/":
        a=stack.pop()
        b=stack.pop()
        stack.append(b//a)
    else:
        stack.append(int(i))
for i in stack:
    print(i)