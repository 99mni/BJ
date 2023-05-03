def Check():
	A[0] = min(A[0], N-A[0]+1)
	for i in range(1, N):
		if (A[i] > N-A[i]+1):
			t1, t2 = N-A[i]+1, A[i]
		else:
			t1, t2 = A[i], N-A[i]+1
		if (t1 >= A[i-1]):
			A[i] = t1
		elif(t2 >= A[i-1]):
			A[i] = t2
		else:
			return "NO"
	return "YES"
import sys
input = sys.stdin.readline
T = int(input())
R=[]
for t in range(T):
	N = int(input())
	A = list(map(int, input().split()))
	R.append(Check())
print("\n".join(R))