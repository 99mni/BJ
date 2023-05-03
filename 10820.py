import sys
while True:
    L=sys.stdin.readline()
    if not L: break
    m,c,n,s=0,0,0,0
    ll=len(L)
    for i in range(0,ll):
        if (L[i]==' '): s+=1
        elif( (ord(L[i])>=ord('a')) and (ord(L[i])<=ord('z')  ) ):
            m+=1
        elif( (ord(L[i])>=ord('A')) and (ord(L[i])<=ord('Z')  ) ):
            c+=1
        elif( (ord(L[i])>=ord('0')) and (ord(L[i])<=ord('9')  ) ):
            n+=1
    print(m,c,n,s)    