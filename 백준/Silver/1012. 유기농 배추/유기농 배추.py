import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    m,n,k = map(int,sys.stdin.readline().split())
    cablist = []
    doneli = []
    nowli = []
    count = 0
    
    for i in range(k):
        a,b = map(int,sys.stdin.readline().split())
        cablist.append([a,b])
    
    for i in cablist:    
        if i in doneli: # 이미 탐색했으면 볼 필요 X
            pass
        
        else:
            nowli = deque([i]) # queue 구조 사용 위해서 덱
            doneli.append(i)
            
            while nowli:
                x = nowli[0][0]
                y = nowli[0][1]
                
                if [x+1,y] in cablist and [x+1,y] not in doneli:
                    nowli.append([x+1,y])
                    doneli.append([x+1,y])
                if x >=1 and [x-1,y] in cablist and [x-1,y] not in doneli:
                    nowli.append([x-1,y])
                    doneli.append([x-1,y])
                if [x,y+1] in cablist and [x,y+1] not in doneli:
                    nowli.append([x,y+1])
                    doneli.append([x,y+1])
                if y >= 1 and [x,y-1] in cablist and [x,y-1] not in doneli:
                    nowli.append([x,y-1])
                    doneli.append([x,y-1])
                nowli.popleft() # Queue 구조, FIFO
                
            count += 1 # 한 개의 group 탐색끝날 때마다 +1
    print(count)