N, K = map(int, input().split())
S = input()
A= list(S[0:K-1])
diff=ord('a')-ord('A')
for i in range(K-1,N):
	if (ord(S[i])>ord('a')):
		A.append(chr(ord(S[i])-diff))
	else:
		A.append(chr(ord(S[i])+diff))
print(''.join(A))
