T=int(input())
for t in range(1,T+1):
    s=input()
    c=0
    for i in range(len(s)):
        if (ord(s[i])-ord('a'))==i: c+=1
        else: break
    print(f'#{t} {c}')