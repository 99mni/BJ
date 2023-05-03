import sys
input=sys.stdin.readline
N=int(input())
R=[]
for i in range(N):
    l1=input().strip()
    l2=input().strip()
    R.append("Case "+str(i+1)+": "+l2+", "+l1)
print("/n".join(R))