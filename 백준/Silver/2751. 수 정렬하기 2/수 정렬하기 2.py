import sys

N = int(sys.stdin.readline())
L =[]
for i in range(N):
    L.append(int(sys.stdin.readline()))
for i in sorted(L):
    print(i)