def CanSee(a, b):
	dh, dv = b-a, H[b]- H[a]
	for i in range(a+1, b):
		if ( (dh* H[a] + dv*(i-a)) <=  (dh* H[i])):
			return False
	return True

N = int(input())
H = list(map(int, input().split()))

C =[]
for i in range(0, N):
	C.append(0)
for i in range(0, N):
	for j in range(i+1, N):
		if (CanSee(i,j)==True):
			C[i], C[j] = C[i]+1, C[j]+1
print(max(C))