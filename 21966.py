N=int(input())
S=input()
if(N<=25): print(S)
else:
    if ("." in S[11:-12]):
        print(S[:9]+"......"+S[-10:])
    else: print(S[:11]+"..."+S[-11:])