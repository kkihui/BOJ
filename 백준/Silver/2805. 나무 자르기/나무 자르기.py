import sys

N,M = map(int,sys.stdin.readline().split())
woli = list(map(int,sys.stdin.readline().split()))
hmax = min(max(woli)-1 , max(woli)-M//N)
hmin = max(0, max(woli)-M)

while hmin <= hmax : # 이진탐색으로 높이 설정
    h = (hmax+hmin)//2
    ali = list(map(lambda i: woli[i] - h if woli[i]-h > 0 else 0, range(N)))
    
    if sum(ali) == M:
        break
    elif sum(ali) < M:
        hmax = h-1
    else:
        hmin = h+1

if sum(ali) < M: # M이 딱 안 맞는데 작을 경우, 1 빼줌
    h -= 1

print(h)