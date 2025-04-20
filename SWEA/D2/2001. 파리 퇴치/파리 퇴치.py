T = int(input())

for t in range(1, T + 1):
    matrix = []
    ans = 0
    
    n,m = map(int,input().split())
    
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    
    # 최 좌상단의 row와 col index는 0~n-m까지 가능
    for i in range(n-m+1):
        for j in range(n-m+1):
            killed = 0
            for row in range(i,i+m):
                for col in range(j,j+m):
                    killed += matrix[row][col]
            ans = max(ans,killed)
            
    print(f'#{t} {ans}')