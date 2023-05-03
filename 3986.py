def Good(s):
    S=[]
    ll = len(s)
    for i in range(0,ll):
        if(len(S)==0):
            S.append(s[i])
        elif(S[-1] != s[i]):
            S.append(s[i])
        else:
            S.pop()
    if(len(S)==0):
        return 1
    else:
        return 0

N = int(input())
cnt =0
for i in range(0, N):
    str = input()
    cnt += Good(str)
print(cnt)