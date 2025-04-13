T = int(input())

for t in range(T):
    n = int(input())
    ans = [0]*(n+1)
    candi_a = list(map(int,input().split()))
    candi_b = list(map(int,input().split()))
    
    a_id,b_id = 0,0
    
    while a_id < n:
        if ans[candi_a[a_id]] == 0:
            ans[candi_a[a_id]] = 'A'
            a_id += 1
            while b_id < n:
                if ans[candi_b[b_id]] == 0:
                    ans[candi_b[b_id]] = 'B'
                    b_id += 1
                    break
                else:
                    b_id += 1
        else:
            a_id += 1
    
    for i in range(1,n+1):
        print(ans[i],end='')
    print()
    