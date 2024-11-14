# Matrix 최대 크기는 r*c = 2500

import sys

def search_4way(r,c,mat,add):
    dr = (0,0,1,-1)
    dc = (1,-1,0,0)
    origin = 0
    value = mat[r][c] // 5
    
    for i in range(4):
        r_new = r+dr[i]
        c_new = c+dc[i]
        
        if 0 <= r_new < len(mat) and 0 <= c_new < len(mat[0]):
            if mat[r_new][c_new] != -1:
                origin -= value
                add.append((r_new,c_new,value))
    
    if origin != 0:
        add.append((r,c,origin))
    
    return 0


def change(r,c,mat,temp):
    if temp:
        if mat[r][c]:
            temp.append(mat[r][c])
            mat[r][c] = temp.pop(0)
        else:
            mat[r][c] = temp.pop(0)
            
    elif mat[r][c]:
        temp.append(mat[r][c])
        mat[r][c] = 0
    
    return 0


def main():
    r,c,t = map(int,sys.stdin.readline().split())
    matrix = []
    purifier = []
    
    for i in range(r):
        temp = list(map(int,sys.stdin.readline().split()))
        matrix.append(temp)
        if temp[0] == -1:
            purifier.append(i)
    
    # t초 동안 반복
    for _ in range(t):
        # 1. 확산 - 모든 칸에 대해서 미세먼지 확산 계산해서 마지막에 더해줌
        addition = []
        for row in range(r):
            for col in range(c):
                if matrix[row][col] not in (0,-1):
                    search_4way(row,col,matrix,addition)
                
        for row,col,value in addition:
            matrix[row][col] += value
        
        # 2. 공기 청정기 작동
        # top쪽 우측 -> 상승 -> 좌측 -> 하강
        top = purifier[0]
        temp = []
        for col in range(1,c):
            change(top,col,matrix,temp)
        for row in range(top-1,-1,-1):
            change(row,c-1,matrix,temp)
        for col in range(c-2,-1,-1):
            change(0,col,matrix,temp)
        for row in range(1,top):
            change(row,0,matrix,temp)
        
        # bot쪽 우측 -> 하강 -> 좌측 -> 상승
        bot = purifier[1]
        temp = []
        for col in range(1,c):
            change(bot,col,matrix,temp)
        for row in range(bot+1,r):
            change(row,c-1,matrix,temp)
        for col in range(c-2,-1,-1):
            change(r-1,col,matrix,temp)
        for row in range(r-2,bot,-1):
            change(row,0,matrix,temp)
    
    ans = 0
    for row in range(r):
        for col in range(c):
            if matrix[row][col] not in (0,-1):
                ans += matrix[row][col]
            
    print(ans)
        
if __name__ == "__main__":
    main()