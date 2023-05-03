def IsVowel(ch):
    if((ch=='a')or(ch=='e')or(ch=='i')or(ch=='o')or(ch=='u')):
        return True
    return False

A=input()
n=len(A)-1
while (n>=0):
    if(IsVowel(A[n])==True):
        break
    n=n-1
print(A[0:n+1]+"ntry")
