N, M = map(int,input().split())
a = set()
for _ in range(N):
    a.add(input())

b=set()
for _ in range(M):
    b.add(input())

res = sorted(list(a&b))
print(len(res))
for i in res:
    print(i)