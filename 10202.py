import sys
input = sys.stdin.readline
N = int(input())
R = []
for i in range(N):
    line = list(input().split())
    n = int(line[0])
    l, r, m = 1, 1, 0
    while (l<=n):
        while((l<=n) and (line[l]=='O')):
            l+=1
        if(l>n):
            break
        r= l 
        while((r<=n) and (line[r]=='X')):
            r+=1
        m = max([m,r-l])
        l=r 
    R.append("The longest contiguous subsequence of X's is of length "+str(m))
print('\n'.join(R))