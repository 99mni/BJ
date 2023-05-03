import sys
input = sys.stdin.readline
N, K= input().split()
N, K = int(N), int(K)
S = list(input().split())
t=S[0]
cur = len(t)
for i in range(1,N):
    if(len(S[i])+cur <= K):
        t=t+" "+S[i]
        cur+=len(S[i])
    else:
        print(t)
        t, cur = S[i], len(S[i])
if(len(t)>0):
    print(t)