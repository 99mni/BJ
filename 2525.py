A, B = map(int, input().split())
C= int(input())

hap = B+C
A += hap//60
m = hap%60

if (A>=24):
    A-=24

print(A, m)