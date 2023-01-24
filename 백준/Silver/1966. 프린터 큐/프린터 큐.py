import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n,m = map(int,sys.stdin.readline().split())
    queue = list(map(str,sys.stdin.readline().split()))
    queue[m] += 't' # target에 t 붙혀서 관리
    order = 0
    
    while True:
        best = max(queue)
        if 't' in best:
            best = best[0]
        
        if best in queue[0]:
            if 't' in queue[0]:
                order+=1
                break
            queue.pop(0)
            order +=1
                
        else:
            queue.append(queue.pop(0))
        
    print(order)