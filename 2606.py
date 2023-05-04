from collections import deque
n = int(input())
v = int(input())
g = [[]for i in range(n+1)]
visited=[0]*(n+1)
for i in range(v):
    a, b = map(int, input().split())
    g[a]+=[b]
    g[b]+=[a]
visited[1]=1
Q = deque([1])
while Q:
    c=Q.popleft()
    for i in g[c]:
        if visited[i]==0:
            Q.append(i)
            visited[i]=1

print(sum(visited)-1)
