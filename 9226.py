R=[]
while True:
    L=input()
    if(L=='#'): break
    i=0
    while((i<len(L)) and ((L[i] in ['a','e','i','o','u'])== False)):
        i+=1
    ss=L[i:]+L[:i]+'ay'
    R.append(ss)
print('\n'.join(R))