a, b, c = map(int, input().split())

if a==b==c:
    m=10000+(a*1000)
elif a==b or a==c:
    m=1000+a*100
elif b==c:
    m=1000+b*100
else:
    m=max(a,b,c)*100

print(m)