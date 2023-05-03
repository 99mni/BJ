def Check(exp):
    stack, ll = [], len(exp)
    for i in range(0, ll):
        if(exp[i]=='('):
            stack.append(1)
        else:
            if(stack):
                stack.pop()
            else:
                return 'NO'
    if(stack):
        return 'NO'
    return 'YES'
N = int(input())
for i in range(N):
    print(Check(input()))