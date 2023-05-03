b = list(input())
l=len(b)
stack=[]
ans = 0
tmp =1

for i in range(l):
    if b[i] == "(":
        stack.append(b[i])
        tmp*=2
    
    elif b[i]=="[":
        stack.append(b[i])
        tmp*=3
    
    elif b[i]==")":
        if not stack or stack[-1] != "(":
            ans =0
            break
        if b[i-1] == "(":
            ans += tmp
        stack.pop()
        tmp//=2
    elif b[i]=="]":
        if (not stack) or (stack[-1] != "["):
            ans =0
            break
        if b[i-1] == "[":
            ans += tmp
        stack.pop()
        tmp//=3

if stack:
    print(0)
else:
    print(ans)