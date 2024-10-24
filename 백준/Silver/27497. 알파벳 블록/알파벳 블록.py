import sys
import collections 

def last_del(deque,last):
    if deque:
        if last.pop() == 1:
            deque.pop()
        else:
            deque.popleft()
    
            
def main():
    deque = collections.deque()
    n = int(sys.stdin.readline())
    last = []
    for _ in range(n):
        command = list(map(str,sys.stdin.readline().split()))
        if command[0] == '1':
            deque.append(command[1])
            last.append(1)
        elif command[0] == '2':
            deque.appendleft(command[1])
            last.append(2)
        else:
            last_del(deque,last)
    
    ans = ''
    for c in list(deque):
        ans += c
    
    if ans:
        print(ans)
    else:
        print(0)
    
if __name__ == "__main__":
    main()
