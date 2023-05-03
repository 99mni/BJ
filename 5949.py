N=input()
A=[]
le=len(N)
for i in range(le):
    A.append(N[le-1-i])
    if(i%3==2):
        A.append(',')
if(A[-1]==','):
    A=A[0:-1]
A.reverse()
print(''.join(A))
