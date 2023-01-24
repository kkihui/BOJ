import sys
from traceback import print_list

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    hli = []
    H,W,N = map(int,sys.stdin.readline().split())
    for i in range(1,W+1): # 호텔 객실 만들기
        for k in range(1,H+1):
            if len(str(i)) == 1:
                hli.append(str(k)+'0'+str(i))
            else:
                hli.append(str(k)+str(i))    
    print(hli[N-1])