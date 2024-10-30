import sys
              
def main():
    n,m = map(int,sys.stdin.readline().split())
    area = 0
    block = []
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(n):
        li = list(map(int,sys.stdin.readline().split()))
        block.append(li)
        area += sum(li)*6
    for i in range(n):
        for j in range(m):
            # 위 아래로 겹치는 부분 빼주기
            area -= (block[i][j] - 1) * 2
            
            # 상하좌우에 있는 블럭과 옆면으로 겹치는 부분 빼주기
            for k in range(4):
                row = i+dx[k]
                col = j+dy[k]
                if 0 <= row and row < n and 0 <= col and col < m:
                    area -= min(block[i][j],block[row][col])
                 
    print(area)
    
    
if __name__ == "__main__":
    main()