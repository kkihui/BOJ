import sys
from collections import deque
         
def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        switch = 1
        func = sys.stdin.readline().rstrip()
        length = int(sys.stdin.readline())
        arr = sys.stdin.readline()[1:-2]
        arr = list(arr.split(","))
        deq = deque(arr)
        
        if func.count('D') > length:
            print("error")
        else:
            for _ in range(len(func)):
                if func[_] == 'R':
                    switch *= -1
                else:
                    if switch == 1: # 정방향
                        deq.popleft()
                    else: # 역방향
                        deq.pop()
            
            arr = list(deq)
            if switch == -1:
                arr = arr[::-1]
            
            last = len(arr)
            print("[",end='')
            for _ in range(last):
                if _ != last-1:
                    print(arr[_],end=',')
                else:
                    print(arr[_],end='')
            print("]")
        
        
if __name__ == "__main__":
    main()