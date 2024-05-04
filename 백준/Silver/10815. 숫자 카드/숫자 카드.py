N = int(input())
N_list = list(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))

dic = {}

for i in M_list:
    dic[i]=0

for i in N_list:
    if i in dic:
        dic[i]=1

for i in dic:
    print(dic[i], end=' ')