T = int(input())
for t in range(0,T):
    N = int(input())
    b= input()
    print("Case #"+str(t+1)+":",end='')
    for i in range(0, N):
        u = 0
        res = ""
        for j in range(0, 8):
            u = u*2
            if(b[i*8+j] == 'I'):
                u = u+1
        res = res + chr(u)
        print(chr(u),end='')
    print()
