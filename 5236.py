R=[]
N= int(input())
for i in range(N):
    A=input()
    loc=len(A)-1
    while(loc-1>=0):
        if(ord(A[loc-1])<=ord(A[loc])):
            break
        loc=loc-1
    R.append("The longest decreasing suffix of "+ A+" is "+(A[loc:]))
print('\n'.join(R))
    
