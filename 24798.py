L, w=map(int,input().split())
if( (w<L)or w>(L*26)):
    print("impossible")
else:
    b=w//L
    r=w%L
    tt=[chr(b-1+ord('a'))]*(L-r)
    tt+=[chr(b+ord('a'))]*r
    print(''.join(tt))
