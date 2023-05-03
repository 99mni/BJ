import sys
input = sys.stdin.readline
N = int(input())
C= []
for i in range(N):
    C.append(list(map(int, input().split)))
C.sort()
mm = 1000000
for i in range(0, N-1):
    if (C[i][1] != C[i+1][1]):
        mm = min([mm,C[i+1][0]-C[i][0]])
pre, cnt =-1,1
for i in range(N):
	if (C[i][1] ==0):
		continue
	if (pre != -1):
		tt = C[i][0] -pre
		if (tt >= mm):
			cnt=cnt+1
	pre = C[i][0]
print(cnt)