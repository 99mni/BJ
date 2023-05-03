import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
av = sum(A)//N
mv = 0 
for i in range(N):
    A[i]-=av
for i in range(N-1):
    mv+=abs(A[i])
    A[i+1]+=A[i]
print(mv)