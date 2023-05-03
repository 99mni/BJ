N= int(input())
for i in range(N):
    T=list(input().split())
    T.reverse()
    print("Case #"+str(i+1)+":",' '.join(T))