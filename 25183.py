N=int(input())
S=input()

def Check():
    cnt=1
    for i in range(len(S)-1):
        if(abs(ord(S[i])-ord(S[i+1]))==1):
            cnt=cnt+1
            if (cnt==5):
                return "YES"
        else:
            cnt=1
    return "NO"

print(Check())