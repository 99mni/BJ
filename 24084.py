N=int(input())
S=input()
R=[]
for i in range(1,N):
    if(S[i]=='J'): R.append(S[i-1])
print("\n".join(R))