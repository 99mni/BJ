import sys
ss=0
for line in sys.stdin:
    line=line.strip()
    if (not line):
        break #끝에 '\n' 입력돼서 제거해야 함
    n=line[0:-3]+line[-2:]
    ss+=int(n)#ValueError: invalid literal for int() with base 10: '\n'

ff=ss%100
if(ff<10):
    rr=str(ss//100)+".0"+str(ff)
else:
    rr=str(ss//100)+"."+str(ff)

print(rr)
