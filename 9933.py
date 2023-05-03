def Check():
	ss = set([])
	pp = input().strip()
	ss.add(pp)
	for i in range(N-1):
		tt = input().strip()
		if (((tt in ss)== True) or (tt[0] != pp[-1])) :
			return ("Player "+str((i+1)%2 +1) +" lost")
		ss.add(tt)
		pp = tt
	return "Fair Game"

import sys
input = sys.stdin.readline
N = int(input())
print(Check())
