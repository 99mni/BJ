a = int(input())
for i in range(a):
    L = []
    R = []
    str= input()
    N = len(str)
    for i in range(0, N):
        if ( str[i] == '<'):
            if(L):
                t = L.pop()
                R.append(t)
        elif(str[i]=='>'):
            if(R):
                t = R.pop()
                L.append(t)
        elif(str[i]=='-'):
            if(L):
                t = L.pop()
        else:
            L.append(str[i])
    for i in range(0, len(L)):
        print(L[i], end='')
    for i in range(0, len(R)):
       print(R[len(R)-i-1], end='')
    print()