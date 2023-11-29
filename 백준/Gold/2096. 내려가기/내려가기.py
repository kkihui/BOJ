import sys
          
def main():
    n = int(sys.stdin.readline())
    dp = [[[0]*2 for _ in range(3)] for _ in range(2)]
    ans_min,ans_max = 900000,0
    
    temp = tuple(map(int,sys.stdin.readline().split()))
    for i in range(3):
        for j in range(2):
            dp[0][i][j] = temp[i]
            
    for _ in range(1,n):
        temp = tuple(map(int,sys.stdin.readline().split()))
            
        for j in range(3):
            if j == 0: # 제일 왼쪽은 [0] [1] 탐색
                min_num = min(dp[0][0][1],dp[0][1][1])
                max_num = max(dp[0][0][0],dp[0][1][0])
            elif j == 1: # 가운데는 [0] [1] [2] 싹다 탐색
                min_num = min(dp[0][0][1],dp[0][1][1],dp[0][2][1])
                max_num = max(dp[0][0][0],dp[0][1][0],dp[0][2][0])
            else: # 제일 오른쪽은 [1] [2] 탐색
                min_num = min(dp[0][1][1],dp[0][2][1])
                max_num = max(dp[0][1][0],dp[0][2][0])
            dp[1][j][0] = temp[j] + max_num
            dp[1][j][1] = temp[j] + min_num
        
        for j in range(3):
            dp[0][j][0] = dp[1][j][0]
            dp[0][j][1] = dp[1][j][1]

    for i in range(3): # 한 줄만 주어지는 경우 대비해서 dp[0] 쪽을 봄. (여러 줄도 어차피 복사해놔서 ㄱㅊ)
        ans_max = max(ans_max,dp[0][i][0]) 
        ans_min = min(ans_min,dp[0][i][1])
        
    print(ans_max,ans_min)
    
if __name__ == "__main__":
    main()