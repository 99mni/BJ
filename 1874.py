n = int(input())
stack, ans, find = [], [], 0
a = 1
for i in range(n):
    num = int(input())
    while a <= num:
        stack.append(a)
        ans.append("+")
        a += 1

    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        find = 1
        break

if find == 0:
    for i in ans:
        print(i)
