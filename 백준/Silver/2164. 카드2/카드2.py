#덱을 활용하면 시간복잡도 O(1)로 쉽게 왼쪽에서 빼서 오른쪽으로 넣을 수 있다.
from collections import deque

N = int(input())
deq = deque()
for _ in range(1,N+1):
    deq.append(_)
while len(deq) != 1:
    deq.popleft()
    deq.append(deq.popleft())
print(deq.popleft())