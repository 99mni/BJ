s=input()
l=len(s)
s1=s[:l//2]
s2=s[l//2:l]
t1=sum(list(map(int,list(s1))))
t2=sum(list(map(int,list(s2))))
if(t1==t2):
    print('LUCKY')
else: print('READY')