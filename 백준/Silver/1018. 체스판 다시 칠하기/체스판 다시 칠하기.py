import sys

Wli = [['W']*8 for _ in range(8)]
Bli = [['B']*8 for _ in range(8)]

for _ in range(8): # 정답인 체스판 만들기
    if _%2 == 1:
        Wli[_][0]='B'
        Bli[_][0]='W'
    for i in range(7):
        if Wli[_][i] == 'W':
            Wli[_][i+1] = 'B'
        if Bli[_][i] == 'B':
            Bli[_][i+1] = 'W'

N,M = map(int,sys.stdin.readline().split())
mnli= [list(sys.stdin.readline().rstrip()) for _ in range(N)]
countli = []

for _ in range(N-7): # 모든 경우로 쪼개고 비교 #50*50이면 43*43*(64+8) = 13만 번 계산
    for i in range(M-7):
        sublist = []
        for j in range(_,_+8):
            sublist.extend([mnli[j][i:i+8]])
        Wcount = 0
        Bcount = 0
        for x in range(8): # 정답list랑 비교해서 다르면 count 올림
            for y in range(8):
                if Wli[x][y] != sublist[x][y]:
                    Wcount += 1
                if Bli[x][y] != sublist[x][y]:
                    Bcount += 1
        countli.append(min(Wcount,Bcount))

print(min(countli))