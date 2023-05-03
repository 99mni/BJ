import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
	B.append([A[i], i])

B.sort()

R =[-1]*N
for i in range(N):
	R[B[i][1]]  = B[N-i-1][0]

R = list (map(str, R))
print(' '.join(R))