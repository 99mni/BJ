import sys
sys.setrecursionlimit(300000)

def dfs(node):
    for i in graph[node]:
        if not visited[i]:
            visited[i] = visited[node]+1
            dfs(i)

n = int(input())
graph = [[] for _ in range(n+1)]
a, b = map(int,input().split())
m = int(input())
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0]*(n+1)

dfs(a)

print(visited[b] if visited[b] > 0 else -1)