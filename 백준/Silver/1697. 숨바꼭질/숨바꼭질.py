import sys

xli = [0]*200001
N,K = map(int,sys.stdin.readline().split())
if N >= K : #N이 더 크면 걸어서 오는 수 밖에 없음
    print(N-K)
    exit()
for _ in range(N,0,-1):# 거꾸로 갔다가 앞으로 가는 경우 생각
    if xli[_-1] == 0:
        xli[_-1] = xli[_]+1         
for _ in range(0,K+1): # 0에서 K까지 가는 경우
    if _ == N-1: # N으로 올때 오염되지 않게 처리해줌
        xli[_+1] = 0
    else:
        if xli[_+1] == 0 :
            xli[_+1] = xli[_]+1
        else:
            xli[_+1] = min(xli[_+1],xli[_]+1)

        if xli[_*2] == 0:
            xli[_*2] = xli[_]+1
        else:
            xli[_*2] = min(xli[_*2],xli[_]+1)
        if _ != N and xli[_] < xli[_-1]:
            xli[_-1] = xli[_]+1
            xli[(_-1)*2] = min(xli[(_-1)*2],xli[_-1]+1)
            xli[_-2] = min(xli[_-2],xli[_-1]+1)
        
for _ in range(2*K,N,-1): # 2k에서 거꾸로 다시 해줌
    if xli[_] == 0:
        xli[_] = min(xli[_+1],xli[_-1])+1
    if xli[_] < xli[_-1]:
        xli[_-1] = xli[_]+1
print(xli[K])