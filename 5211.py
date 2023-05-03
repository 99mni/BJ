s=input().split('|')
a, b = 0, 0
for i in s:
    if s[0] in ['C', 'F', 'G']:
        a+=1
    elif s[0] in ['A', 'D', 'E']:
        b+=1
if(a==b):
    if s[-1][-1] in ['C', 'F', 'G']:
        a+=1
    elif s[-1][-1] in ['A', 'D', 'E']:
        b+=1
if(a>b): 
    print("C-major")
else:
    print("A-minor")