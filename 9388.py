import sys
input = sys.stdin.readline

def Conv(s):
    u=[]
    de=ord('A')-ord('a')
    for i in range(len(s)):
        if((ord(s[i])>=ord('A'))and(ord(s[i])<=ord('Z'))):
           u.append(chr(ord(s[i])-de))
        elif((ord(s[i])>=ord('a'))and(ord(s[i])<=ord('z'))):
             u.append(chr(ord(s[i])+de))
        else:
            u.append(s[i])
    return (''.join(u))

def Check(a,b):
    if(a==b):
        return("Login successful.")
    if(a==Conv(b)):
        return("Wrong password. Please, check your caps lock key.")
    nl=[]
    for i in range(len(a)):
        if((ord(a[i])>=ord('A'))and(ord(a[i])<=ord('Z'))):
           nl.append(a[i])
        elif((ord(a[i])>=ord('a'))and(ord(a[i])<=ord('z'))):
           nl.append(a[i])
    nl=''.join(nl)
    if(nl==b):
             return("Wrong password. Please, check your num lock key.")
    if (nl==Conv(b)):
        return("Wrong password. Please, check your caps lock and num lock keys.")
    return ("Wrong password.")

R=[]
N=int(input())
for i in range(N):
    p,e=input().split()
    R.append("Case "+str(i+1)+": "+Check(p,e))

print('\n'.join(R))
