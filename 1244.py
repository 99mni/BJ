import sys
input = sys.stdin.readline
T=int(input())
A = list(map(int, input().split()))
A = list(map(bool, A))
bb = bool(1)
N = int(input())
for i in range(N):
	s, n = map(int, input().split())
	if (s ==1):
		loc = n-1
		while (loc<T):
			A[loc] ^= bb
			loc = loc+n
	else:
		i, n = 1, n-1
		A[n] ^= bb
		while (n+i<T and n-i>=0):
			if (A[n+i] != A[n-i]):
				break
			A[n+i] ^=bb
			A[n-i] ^=bb
			i=i+1

A = list(map(int, A))
A = list(map(str,A))
ll = len(A)//20
for i in range(ll):
	print(' '.join(A[i*20:i*20+20]))
tt = len(A) %20
if (tt != 0):
	print(' '.join(A[-tt:]))