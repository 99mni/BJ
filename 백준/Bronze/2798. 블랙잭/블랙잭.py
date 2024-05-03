N, M = map(int,input().split())
c = list(map(int,input().split()))
res = 0

for i in range(0, len(c)-2):
    for j in range(i+1,len(c)-1):
        for k in range(j+1,len(c)):
            num = c[i]+c[j]+c[k]
            if res<num<M: 
                res=num
            elif num==M: 
                res=num
                break

print(res)