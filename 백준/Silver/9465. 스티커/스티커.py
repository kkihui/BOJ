import sys

def main():
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        N = int(sys.stdin.readline())
        sticker = [0]*2
        for i in range(2):
            sticker[i] = list(map(int,sys.stdin.readline().split()))
        
        dp = [[0]*N for _ in range(2)]
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        
        for i in range(1,N):
            if i == 1:
                dp[0][i] = dp[1][i-1] + sticker[0][i]
                dp[1][i] = dp[0][i-1] + sticker[1][i]
            else:
                # 선택 안 하는 경우 고려
                dp[0][i] = max(dp[1][i-1],dp[1][i-2],dp[0][i-2]) + sticker[0][i]
                dp[1][i] = max(dp[0][i-1],dp[1][i-2],dp[0][i-2]) + sticker[1][i]
                        
        
        print(max(max(dp[0]),max(dp[1])))

if __name__ == '__main__':
    main()

''' greedy 하게 하지 말고 각 열별로 dp로 해보기
import sys

dx = (1,-1,0,0)
dy = (0,0,-1,1)
def main():
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        N = int(sys.stdin.readline())
        sticker = [0]*2
        ans = 0
        for i in range(2):
            sticker[i] = list(map(int,sys.stdin.readline().split()))
        
        # point = [[0]*N for _ in range(2)]
        
        for _ in range(3):
            point = [[0]*N for _ in range(2)]
            for i in range(2):
                for j in range(N):
                    point[i][j] += sticker[i][j]
                    for k in range(4):
                        new_x = j+dx[k]
                        new_y = i+dy[k]
                        if 0 <= new_x and new_x < N and 0<= new_y and new_y < 2:
                            point[i][j] -= sticker[new_y][new_x]
                    if point[i][j] > 0:
                        ans += sticker[i][j]
                        sticker[i][j] = 0
                        for k in range(4):
                            new_x = j+dx[k]
                            new_y = i+dy[k]
                            if 0 <= new_x and new_x < N and 0<= new_y and new_y < 2:
                                sticker[new_y][new_x] = 0
                        
        
        print(point)
        
        print(sticker)
        
        print(ans)

if __name__ == '__main__':
    main()
'''