import sys 
sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(start, depth):
    visited[start] = True
    for i in g[start]:
        if not visited[i]:
            dfs(i, depth+1)

N, M = map(int,input().split())
g = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False]*(N+1)
cnt =0 
for i in range(1,N+1):
    if not visited[i]:
        if not g[i]:
            cnt += 1
            visited[i]=True
        else:
            dfs(i,0)
            cnt+=1

print(cnt)
