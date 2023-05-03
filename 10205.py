import sys
input=sys.stdin.readline
N=int(input())
R=[]
for i in range(N):
    B=int(input())
    A=input()
    c=A.count('c')
    b=A.count('b')
    R.append('Data Set '+str(i+1)+':\n'+str(B+c-b)+'\n')

print('\n'.join(R))
