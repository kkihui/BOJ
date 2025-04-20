# 최대 50개의 점의 좌표와 +_ 0.1 위치 살펴보기 (최대 150*50) 탐색
 
T = int(input())
 
for t in range(T):
    n = int(input())
    a_n = list(map(int,input().split()))
    candinate = set()
    ans,linear = 0,0
     
    for a in a_n:
        candinate.add(a)
        candinate.add(a-0.1)
        candinate.add(a+0.1)
     
    for num in candinate:
        cnt = 0
         
        if linear:
            ans = -1
            break
         
        for i in range(1,n):
            if a_n[i] == a_n[i-1]:
                linear = 1
                break
            elif a_n[i] > a_n[i-1]:
                if i == n-1:
                    if a_n[i] >= num and num >= a_n[i-1]:
                        cnt += 1
                else:
                    if a_n[i] > num and num >= a_n[i-1]:
                        cnt += 1  
            else:
                if i == n-1:
                    if a_n[i] <= num and num <= a_n[i-1]:
                        cnt += 1
                else:
                    if a_n[i] < num and num <= a_n[i-1]:
                        cnt += 1
                 
        ans = max(ans,cnt)
 
    print(ans)