def Check(tt):
    for i in range(9):
        if (P[i]=='*'):
            continue
        if(P[i]!=tt[i]):
            return False
        return True

P=input()
N=int(input())
R=[]
for i in range(N):
    ll=input().strip()
    if(Check(ll)==True):
        R.append(ll)

print(len(R))
print('\n'.join(R))
