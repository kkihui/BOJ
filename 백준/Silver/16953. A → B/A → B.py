import sys
from collections import deque

def main():
    A,B = map(int,sys.stdin.readline().split())
    visit = set()
    queue = deque()
    queue.append((A,0))
    serached = 0
    while queue != deque():
        num,len = queue.pop()
        for _ in range(2):
            if _ == 0:
                new = num*2
            else:
                new = num*10+1

            if new < B and new not in visit:
                visit.add(new)
                queue.append((new,len+1))
            elif new == B:
                print(len+2)
                serached = 1
                break
    if not serached:
        print(-1)


if __name__ == '__main__':
    main()