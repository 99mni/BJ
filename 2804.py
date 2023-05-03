A, B = input().split()
la, lb = len(A), len(B)
M=[]
for i in range(0, lb):
    m = []
    for j in range(0, la):
        m.append('.')
    M.append(m)

for r in range(0,la):
    c=B.find(A[r])
    if (c!=-1): break

r, c = c, r
for i in range(0, la):
    M[r][i] = A[i]
for i in range(0, lb):
    M[i][c] = B[i]

for i in range(0, lb):
    print(''.join(M[i]))