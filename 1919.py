s1=input()
s2=input()
cnt1=[0]*26
cnt2=[0]*26
le=len(s1)
for i in range(0,le):
    cnt1[ord(s1[i])-ord('a')]+=1
le=len(s2)
for i in range(0,le):
    cnt2[ord(s2[i])-ord('a')]+=1
t=0
for i in range(0,26):
    t=t+abs(cnt1[i]-cnt2[i])
print(t)
