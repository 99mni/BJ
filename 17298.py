n = int(input())
seq = list(map(int, input().split()))
o = [-1]*n
st = []

for i in range(n):
    while st and seq[st[-1]]<seq[i]:
        idx = st.pop()
        o[idx] = seq[i]
    st.append(i)

print(*o)
