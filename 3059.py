T=int(input())
for t in range(0,T):
    S=input()
    A=[]
    for i in range(0,26):
        A.append(1)
    le=len(S)
    for i in range(0,le):
        A[ord(S[i])-ord('A')]=0
    ss=0
    for j in range(0,26):
        ss=ss+A[i]*(ord('A')+i)
    print(ss)