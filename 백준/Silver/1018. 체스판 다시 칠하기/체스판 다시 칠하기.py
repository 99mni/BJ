N, M = map(int,input().split())
l=[]
cnt=[]

for i in range(N): l.append(input())

for a in range(N-7):
    for b in range(M-7):
        w_index = 0
        b_index = 0
        for i in range(a, a+8):
            for j in range(b,b+8):
                if (i+j)%2==0:
                    if l[i][j]!='W':
                        w_index +=1
                    else: b_index+=1
                else:
                    if l[i][j]!='W':
                        b_index +=1
                    else: w_index+=1
        cnt.append(w_index)
        cnt.append(b_index)

print(min(cnt))