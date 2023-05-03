N=int(input())
ss=set(['he','she','him','her'])
W=list(input().split())
cnt=0
for w in W:
    if((w in ss)==True):
        cnt+=1
print(cnt)
