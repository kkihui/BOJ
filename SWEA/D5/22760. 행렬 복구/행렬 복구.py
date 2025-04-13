# 주대각선은 겹치는걸로 찾을 수 있음
# 1번째 행을 아무거나 고정시키면 A이든 A^T이든 나머지 소거해서 맞춰나갈 수 있음 

T = int(input())

for t in range(T):
    n = int(input())
    A,B = [],[]
    num_set = set(range(1,n**2+1))
    candi = [[] for _ in range(n)]
    
    for _ in range(2*n):
        row = list(map(int,input().split()))
        B.append(row)
    
    for col in range(n):
        col_set = set()
        dia = 0
        for row in range(2*n):
            if B[row][col] in col_set:
                dia = B[row][col]
                break
            else:
                col_set.add(B[row][col])
        if dia:
            for row in range(2*n):
                if B[row][col] == dia:
                    candi[col].append(B[row])
    
    for row in range(n):
    	# 1번째 행은 암거나 골라주기
        if row == 0:
            A_row = candi[row][0]
        else:
            # 2번째 행부터는 안 쓴 숫자만 있는거 하면 하나로 결정됨.
            for i in range(2):
                if set(candi[row][i]) <= num_set:
                    A_row = candi[row][i]
        num_set = num_set - set(A_row)    
        A.append(A_row)
            
    for row in A:
        print(*row)
    

        