import sys
imput = sys.stdin.readline
N = int(input())
G, L = [], []
for i in range(N):
    gl, ll = input().split()
    if (gl=="G"):
        G.append(int(ll))
    else:
        L.append(int(ll))
G.sort()
L.sort()
gl, ll = len(G), len(L)
loc = ll -1
mm=100000000
cnt=0
for i in range(gl-1,-1,-1):
    while(loc>=0 and L[loc]>=G[i]):
        cnt, loc = cnt+1, loc-1
    rm = gl-1 -i + (ll-cnt)
    mm=min([mm,rm])
print(mm)