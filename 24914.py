import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
A =[0]*N
R=[]
me, mm, tot =0, 0, 0
for i in range(Q):
	q, n1, n2 = map(int, input().split())
	if (q==1):
		if (n2 == N+1):
			me += n1
		else:
			A[n2-1] += n1
			mm = max([mm, A[n2-1]])
			tot += n1
	else:
		bme = me + n1
		if (bme <= mm):
			R.append("NO")
			continue
		if (tot + n2 <= (bme-1)*N):
			R.append("YES")
		else:
			R.append("NO")
print("\n".join(R))
