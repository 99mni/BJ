N=int(input())
pt=input().split('*')
for _ in range(N):
    ss=input()
    if (ss[:len(pt[0])]==pt[0] 
    and ss[-len(pt[1]):]==pt[1] 
    and len("".join(pt))<=len(ss)):
        print("DA")
    else:
        print("NE")