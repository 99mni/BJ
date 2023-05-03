import sys
input = sys.stdin.readline()
str = list(input())
st = []
n = int(input())

for i in range(n):
    c = input().split()
    if c[0] == "L" and str:
        st.append(str.pop())
    elif c[0] == "D" and st:
        str.append(st.pop())
    elif c[0] == "B" and str:
        str.pop()
    elif c[0] == "P":
        str.append(c[1])

print("".join(str + list(reversed(st))))