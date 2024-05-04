import sys
input = sys.stdin.readline

N, M = map(int,input().split())
pok = {}
num = {}
for i in range(1, N+1):
    p=input().strip()
    pok[i] = p
    num[p] = i

for _ in range(M):
    a = input().strip()
    if a.isdigit():
        print(pok[int(a)])
    else:
        print(num[a])