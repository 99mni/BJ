def GetIdx(c):
    if(ord(c)<=ord('Z')):
        return (ord(c)-ord('A'))
    else:
        return (ord(c)-ord('a'))
def Accel(ss):
        for i in range(0,N):
            ff=ss.split()
            ll=len(ff)
            for j in range(0,ll):
                    t=GetIdx(ff[j][0])
                    if(F[t]==False):
                        F[t]=True
                        ff[j]="["+ff[j][0]+"]"+ff[j][1:]
                        ans=""
                        for j in range(0,ll-1):
                            ans = ans+ff[j]+" "
                        ans = ans +ff[-1]
                        return ans

        for i in range(0,N):
            ll=len(ss)
            for j in range(1,11):
                if(ss[j]==' '):
                    continue
                t=GetIdx(ss[j])
                if (F[t]==False):
                    F[t]=True
                    ans=ss[0:j]+"["+ss[j]+"]"+ss[j+1:]
                    return ans
        return ss
    
F=[]
for i in range(0, 26):
        F.append(False)

N = int (input())
for i in range(0,N):
	print(Accel(input()))
    
                                             
                
