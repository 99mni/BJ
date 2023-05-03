n = int(input())
s = input()
stack=[]
cnt = [0]*n

for i in range(n):
    if s[i]=='(':
        stack.append(i)
    else:
        if stack:
            cnt[i]=cnt[stack[-1]]=1
            stack.pop()
ans = 0
count =0
for num in cnt:
    if num ==1:
        count +=1
        ans = max(ans,count)
    else:
        count=0
print(ans)