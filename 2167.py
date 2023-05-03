N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
for _ in range(K):
    i, j, x, y = map(int,input().split())
    cnt =0
    for t in range(i-1,x):
        for tt in range(j-1, y):
            cnt += A[t][tt]
    print(cnt)