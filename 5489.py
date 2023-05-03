N = int(input())
C=[0]*10001
for i in range(N):
    C[int(input())]+=1
mm=max(C)
print(C.index(mm))
