import sys
input = sys.stdin.readline

N, M = map(int,input().split())
S = set()
cnt = 0
for _ in range(N):
    word = input().strip()
    S.add(word)

for _ in range(M):
    check = input().strip()
    if check in S:
        cnt += 1

print(cnt)