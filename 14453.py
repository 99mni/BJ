import sys
input = sys.stdin.readline
dic = {'P':0,'H':1,'S':2}
T=[0,0,0]
N = int(input())
A=[]
for i in range(3):
    t = [0]*N
    A.append(t)

for i in range(0,N):
    n=dic[input()[0]]
    for j in range(3):
        A[j][i] = A[j][i-1]
    A[n][i] = A[n][i]+1
    T[n] += 1
mm = max(T)
for i in range(N):
	mm = max([mm, A[0][i] + T[1] - A[1][i], A[0][i] + T[2] - A[2][i]])
	mm = max([mm, A[1][i] + T[0] - A[0][i], A[1][i] + T[2] - A[2][i]])
	mm = max([mm, A[2][i] + T[0] - A[0][i], A[2][i] + T[1] - A[1][i]])
print(mm)