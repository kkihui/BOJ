# 나머지로 정수 크기 줄이면, 테스트 케이스 당 최대 연산 1000*100 = 10만으로 빠르게 가능 
 
import collections
 
num = int(input())
 
for t in range(num):
    s = input()
    deque = collections.deque(list(s))
    k = int(input())
    command = list(map(int,input().split()))
     
    for i in range(k):
        c = command[i]
        if abs(c) >= len(s):
            if c < 0:
                c = -(abs(c)%len(s))
            else: c = c%len(s)
         
        if c < 0:
            for i in range(abs(c)):
                deque.appendleft(deque.pop())
        else:
            for i in range(c):
                deque.append(deque.popleft())
     
    print(''.join(list(deque)))