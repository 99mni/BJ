n = int(input())
A= input()
ss=0
for i in range(0,n):
    ss=ss+ord(A[i])-ord('A')+1
print(ss)