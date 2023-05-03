T = int(input())
R = []
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    dice =1
    for i in range(len(A)):
        if (dice<=A[i]):
            dice += 1
    R.append("Case #"+str(t+1)+": "+str(dice-1))
print("\n".join(R))