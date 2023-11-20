# 0,0 부터 거기까지의 구간합 모두 구해서 이용하기
import sys

def main():
    N,M = map(int,sys.stdin.readline().split())
    matrix = [0]*(N)
    prefixsum = [[0] * N for _ in range(N)]
    xyxy = []
    
    for i in range(N):
        matrix[i] = tuple(map(int,sys.stdin.readline().split()))
    for _ in range(M):
        xyxy.append(tuple(map(int,sys.stdin.readline().split())))
    
    prefixsum[0][0] = matrix[0][0]
    
    for row in range(N):
        for col in range(N):
            if row == 0 and col != 0: # 1번째 row
                prefixsum[row][col] = prefixsum[row][col-1] + matrix[row][col]
            elif row != 0 and col == 0: # 1번째 col
                prefixsum[row][col] = prefixsum[row-1][col] + matrix[row][col]
            elif row != 0 and col != 0: # 위의 케이스 + 0,0 제외한 나머지
                prefixsum[row][col] = prefixsum[row-1][col] + prefixsum[row][col-1] + matrix[row][col] - prefixsum[row-1][col-1]
        
    for now in xyxy: # 최대 10만번 반복하기 때문에 200번 이내로 연산해야함.
        x1,y1,x2,y2 = now
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        if x1 == 0 and y1 == 0:
            ans = prefixsum[x2][y2]
        elif x1 == 0:
            ans = prefixsum[x2][y2] - prefixsum[x2][y1-1]
        elif y1 == 0:
            ans = prefixsum[x2][y2] - prefixsum[x1-1][y2]
        else:
            ans = prefixsum[x2][y2] - prefixsum[x1-1][y2] - prefixsum[x2][y1-1] + prefixsum[x1-1][y1-1] 
        print(ans)
    

if __name__ == '__main__':
    main()