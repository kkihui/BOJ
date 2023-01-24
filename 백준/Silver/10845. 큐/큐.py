import sys
N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    if "push" in s:
        queue.append(int(s[5:]))
    
    if "pop" in s:
        if queue == []:
            print(-1)
        else:
            print(queue.pop(0))
            
    if "size" in s:
        print(len(queue))
        
    if "empty" in s:
        if queue == []:
            print(1)
        else:
            print(0)
    
    if "front" in s:
        if queue == []:
            print(-1)
        else:
            print(queue[0])
        
    if "back" in s:
        if queue == []:
            print(-1)
        else:
            print(queue[-1])