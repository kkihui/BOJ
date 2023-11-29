import sys
from collections import deque

class Graph():
    def __init__(self,n):
        self.graph = [[0] *(n+1) for _ in range(n+1)]
        self.known = set()
        self.party = []
        self.dq = deque()
    
    def bfs(self):
        for people in self.known:
            self.dq.append(people)
        
        while len(self.dq) != 0:
            now = self.dq.popleft()
            for i in range(len(self.graph)):
                if self.graph[now][i] == 1 and i not in self.known:
                    self.dq.append(i)
                    self.known.add(i)        

def main():
    n,m = map(int,sys.stdin.readline().split())
    g = Graph(n)
    ans = 0
    init_member = list(map(int,sys.stdin.readline().split()))
    
    if init_member[0] != 0:
        for i in range(1,init_member[0]+1):
            g.known.add(init_member[i])
    
    for i in range(m): # 노드 사이 연결
        g.party.append(list(map(int,sys.stdin.readline().split())))
        for j in range(1,g.party[i][0]+1):
            for k in range(1,g.party[i][0]+1):
                a = g.party[i][j]
                b = g.party[i][k]
                g.graph[a][b] = 1
                g.graph[b][a] = 1
    
    g.bfs()
    
    for i in range(m):
        can_cnt = 1
        for j in range(1,g.party[i][0]+1):
            if g.party[i][j] in g.known:
                can_cnt = 0
                break
        if can_cnt:
            ans += 1
        
    print(ans)
    
        
if __name__ == "__main__":
    main()