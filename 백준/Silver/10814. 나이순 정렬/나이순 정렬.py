N=int(input())
A = []
for i in range(N):
    age, name = map(str,input().split())
    A.append((int(age),name))

A.sort(key = lambda x : x[0])

for i in A:
    print(i[0], i[1])