num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(str, input().split())
N = N[::-1]
res = 0

for i in range(len(N)):
    res += (int(B)**i)*(num.index(N[i]))

print(res)