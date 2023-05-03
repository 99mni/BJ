R = []
N = int(input())
for i in range(N):
    A = list(map(int, input().split()))
    C = [0]*8
    for j in range(A[0]):
        C[A[2*(j+1)]-1] += 1
    R.append(max(C))
R = list(map(str, R))
print('\n'.join(R))