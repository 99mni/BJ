razor = list(input())
ans = 0
st = []

for i in range(len(razor)):
    if razor[i]=='(':
        st.append('(')
    else:
        if razor[i-1] == '(':
            st.pop()
            ans += len(st)
        else:
            st.pop()
            ans += 1

print(ans)