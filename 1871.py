N=int(input())
B=ord('A')
for i in range(0,N):
    t=input()
    a=(ord(t[0])-B)*26*26+(ord(t[1])-B)*26+(ord(t[2])-B)
    b=int(t[4:8])
    if(abs(a-b)<=100):
        print("nice")
    else:
        print("not nice")
