N, Q = map(int, input().split())
H=[0]*(N+1)
for i in range(N):
    H[i+1]=H[i]+int(input())
R=[]
for i in range(Q):
    st, ed = map(int,input().split())
    R.append(H[ed] - H[st-1])
R = list(map(str, R))
print('\n'.join(R))