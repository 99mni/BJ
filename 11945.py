M, N = map(int, input().split())
for i in range(0, M):
    A = list(input())
    l, r = 0, N-1
    while(l<r):
        A[l], A[r] = A[r], A[l]
        l+=1
        r-=1
    print(''.join(A))
