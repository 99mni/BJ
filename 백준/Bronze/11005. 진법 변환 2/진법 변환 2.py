N, B = map(int,input().split())
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = ''

while N:
    res += str(num[N%B])
    N = N//B

print(res[::-1])