import sys
import copy
R,C,N = map(int,sys.stdin.readline().split())
board1 = []
board2 = [['O']*C for _ in range(R)]

for _ in range(R):
    s = sys.stdin.readline().rstrip()
    board1.append(list(s))

if N == 1 or N%2 == 0: # 1이거나 2의 배수면 굳이 계산 X
    if N == 1:
        ans = board1
    elif N%2 == 0:
        ans = board2
    
    for _ in ans:
        for i in _:
            print(i,end='')
        print()
    exit()

for _ in range(3,N+1): # 1이 아닌 홀수는 N초 동안 반복하며 계산
    full = copy.deepcopy(board2)
    if _%2 == 1:
        for y in range(R):
            for x in range(C):
                if board1[y][x] == 'O':
                    full[y][x] = '.'
                    if y == 0:
                        full[y+1][x] = '.'
                    elif y == R-1:
                        full[y-1][x] = '.'
                    else:
                        full[y-1][x] = '.'
                        full[y+1][x] = '.'
                    
                    if x == 0:
                        full[y][x+1] = '.'
                    elif x == C-1:
                        full[y][x-1] = '.'    
                    else:
                        full[y][x+1] = '.'
                        full[y][x-1] = '.'
        board1 = copy.deepcopy(full)

for i in board1: #최종 출력
    for j in i:
        print(j,end='')
    print()