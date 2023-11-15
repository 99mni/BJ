import sys
input=sys.stdin.readline

N, M = map(int, input().split())
li=[0]*N
for _ in range(M):
    i, j, k = map(int,input().split())
    for i in range(i, j+1):
        li[i-1]=k

for i in range(N):
    print(li[i], end=' ')