import sys
input = sys.stdin.readline
R= []
while True:
    N = int(input())
    if (N==0):
        break
    A = list(map(int, input().split()))
    s=0
    for i in range(len(A)-1, -1 ,-1):
        s = 2*s + A[i]
    R.append(s)
R=list(map(str, R))
print(''.join(R))