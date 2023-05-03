N = int(input())
A = []
for i in range(N):
    A.append(list(input()))
C = int(input())
if (C==2):
    for i in range(N):
        l, r = 0, N-1
        while(l<r):
            A[i][l], A[i][r] = A[i][r], A[i][l]
            l, r = l+1, r-1
elif (C==3):
    for i in range(N):
        u, d =0, N-1
        while(u<d):
            A[u][i], A[d][i] = A[d][i], A[u][i]
            u, d = u+1, d-1
for i in range(N):
    print(''.join(A[i]))