N=int(input())
A=list(input())
f,r=0,N-1
while(f<=r):
    if(A[f]=='?' and A[r]=='?'):
        A[f],A[r]='a','a'
    elif(A[f]=='?'):
        A[f]=A[r]
    elif(A[r]=='?'):
        A[r]=A[f]
    f,r=f+1,r-1

print(''.join(A))
