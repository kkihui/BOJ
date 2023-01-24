import sys
from collections import deque
class minheap:
    def __init__(self):
        self.tree=deque([0])
        self.level = 0
        
    def insert(self,n): # 마지막에 삽입하고 부모와 비교하면서 교환
        self.tree.append(n)
        self.level += 1
        i = self.level
        if self.level > 1:
            while i > 1:
                if self.tree[i] < self.tree[i//2]: # 자식이 부모보다 작으면 교환
                    temp = self.tree[i]
                    self.tree[i] = self.tree[i//2]
                    self.tree[i//2] = temp
                else:
                    break
                i = i//2

    def delmin(self): # 루트 노드 없애고 마지막 노드 넣고 다시 정렬
        if len(self.tree) == 1:
            print(0)
            return 0
        elif len(self.tree) == 2:
            print(self.tree.pop())
            self.level -= 1
            return 0
        else:
            self.tree.popleft() # 0 제거
            print(self.tree.popleft()) #min값 제거
            self.tree.appendleft(self.tree.pop()) 
            self.tree.appendleft(0)
            self.level -= 1
        j = 1
        while 2*j <= self.level:
            if 2*j+1 <= self.level: # 자식이 둘 다 존재하는 경우
                if self.tree[2*j] <= self.tree[2*j+1]: #왼쪽 자식이 작거나 같을 때
                    if self.tree[j] > self.tree[2*j]: # 왼쪽 자식보다 클 때 교환
                        temp = self.tree[j]
                        self.tree[j] = self.tree[2*j]
                        self.tree[2*j] = temp
                        j = 2*j
                    else: # 같거나 크면 교환X
                        break
                else: # 오른쪽 자식이 작을 때
                    if self.tree[j] > self.tree[2*j+1]: # 오른쪽 자식보다 클 때 교환
                        temp = self.tree[j]
                        self.tree[j] = self.tree[2*j+1]
                        self.tree[2*j+1] = temp
                        j=2*j+1
                    else: # 같거나 크면 교환X
                        break
            else: # 왼쪽만 존재하는 경우
                if self.tree[j] > self.tree[2*j]: # 왼쪽 자식보다 클 때 교환
                    temp = self.tree[j]
                    self.tree[j] = self.tree[2*j]
                    self.tree[2*j] = temp
                    j = 2*j
                else: # 같거나 크면 교환X
                    break
            
h = minheap()

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    
    if num == 0:
        h.delmin()
    
    else:
        h.insert(num)