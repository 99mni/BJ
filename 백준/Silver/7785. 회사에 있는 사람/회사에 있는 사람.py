import sys
input = sys.stdin.readline

N = int(input())
dic = {}
for _ in range(N):
    name, state = input().strip().split()
    if state == "enter":
        dic[name] = True
    else: del dic[name]

print("\n".join(sorted(dic.keys(), reverse = True)))