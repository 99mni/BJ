import sys
A=[]
for i in range(0,26):
    A.append(0)
for line in sys.stdin:
    ll=len(line)
    for i in range(0,ll):
        loc=ord(line[i])-ord('a')
        if(loc>=0 and loc<26):
            A[loc]=A[loc]+1
L =[]
for i in range(0,26):
	L.append([A[i], i])
L.sort()

R=[]
ll = len(L)
R.append(L[ll-1][1])
mm = L[ll-1][0]
i =  ll-2
while (L[i][0] == mm and i>=0):
	R.append(L[i][1])
	i = i-1
R.sort()

K = []
ll = len(R)
for i in range(0,ll):
	K.append(chr( ord('a')+ R[i]))

print(''.join(K))