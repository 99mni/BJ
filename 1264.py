while True:
    ss=input()
    cnt=0
    if (ss=='#'):
        break
    for i in ss:
        if i in 'aeiouAEIOU':
            cnt+=1
    print(cnt)