l = sorted(map(int,input().split()))
res = l[0] + l[1] + min(l[2],l[1]+l[0]-1)
print(res)