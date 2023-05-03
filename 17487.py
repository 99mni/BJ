lset=set(list("qwertyasdfgzxcvb"))
ss=input()
ll=len(ss)
l, r, m=0,0,0
de=ord('a')-ord('A')
for i in range(0,ll):
    if (ord(ss[i])==ord(' ')):
        m+=1
    elif( ord(ss[i])>=ord('A') and ord(ss[i])<=ord('Z') ):
        m+=1
        if( (chr(ord(ss[i])+de) in lset)  ==True ):
            l+=1
        else:
            r+=1
    else:
        if( (ss[i] in lset) == True ):
            l+=1
        else: r+=1

if(l>=r):
    d=min(l-r,m)
    r+=d 
    m-=d
    if(m>0):
        if(m%2==1):
            l,r=l+m//2+1,r+m//2
        else: l,r=l+m//2,r+m//2
else:
    d=min(r-l,m)
    l+=d 
    m-=d
    if(m>0):
        if(m%2==1):
            l,r=l+m//2+1,r+m//2
        else: l,r=l+m//2,r+m//2
print(l,r)