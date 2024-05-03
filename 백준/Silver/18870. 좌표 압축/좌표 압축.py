N = int(input())
L = list(map(int,input().split()))
L_set = sorted(set(L))
D = {L_set[i]:i for i in range(len(L_set))}
for i in L:
    print(D[i], end=" ")