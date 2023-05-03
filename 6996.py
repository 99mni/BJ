N=int(input())
B=ord('a')
for i in range(0,N):
    s1,s2=input().split()
    c1=[0]*26
    c2=[0]*26
    if(len(s1)!=len(s2)):
        print(s1,'&',s2,'are NOT anagrams.')
        continue
    for j in range(len(s1)):
                   c1[ord(s1[j])-B]+= 1	
    for j in range(len(s2)):
                   c2[ord(s2[j])-B]+= 1
    same = True
    for j in range(0, 26):
	    if (c1[j] != c2[j]):
	    	same = False
	    	break
    if (same == True):
    	print(s1, '&', s2, 'are anagrams.')
    else:
        print(s1, '&', s2, 'are NOT anagrams.')	
