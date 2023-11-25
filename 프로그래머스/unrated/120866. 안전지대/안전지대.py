def solution(board):
    dr = [-1,-1,-1,0,0,1,1,1]
    dc = [-1,0,1,-1,1,-1,0,1]
    n = len(board)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: # 지뢰인 경우 탐색 시작
                for k in range(8): # 8방향 탐색
                    r = i + dr[k]
                    c = j + dc[k]
                    if 0 <= r < n and 0 <= c < n:
                        if board[r][c] == 0: # 안전지대면 비안전지대로 표시
                            board[r][c] = 2
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                cnt += 1
    
    answer = cnt
    return answer