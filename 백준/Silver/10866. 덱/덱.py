import sys
N = int(sys.stdin.readline())
deque = []
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    if "push_front" in s:
        deque.insert(0,int(s[11:]))
    
    if "push_back" in s:
        deque.append(int(s[10:]))
    
    if "pop_front" in s:
        if deque == []:
            print(-1)
        else:
            print(deque.pop(0))
    
    if "pop_back" in s:
        if deque == []:
            print(-1)
        else:
            print(deque.pop())
    
    if "size" in s:
        print(len(deque))
    
    if "empty" in s:
        if deque == []:
            print(1)
        else:
            print(0)
    
    if "front" in s[:6]:
        if deque == []:
            print(-1)
        else:
            print(deque[0])
        
    if "back" in s[:5]:
        if deque == []:
            print(-1)
        else:
            print(deque[-1])