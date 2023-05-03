import sys
import re

input=sys.stdin.readline
R,idx=[],1
diff=ord('a')-ord('A')
while True:
    pat=input()
    if(pat[0]=='#'):
        break
    pat="["+pat[0]+pat[2]+chr(ord(pat[0])-diff)+chr(ord(pat[2])-diff)+"]"
    R.append("Case "+str(idx)+"\n")
    idx+=1
    n=int(input())
    for i in range(n):
        line=input()
        R.append(re.sub(pat,'_',line))
    R.append("\n")
print(''.join(R))
