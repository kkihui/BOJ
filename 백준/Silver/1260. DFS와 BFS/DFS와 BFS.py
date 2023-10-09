import sys
import queue

class Graph:
    def __init__(self,node,start):
        self.graph = [[0]*node for _ in range(node)]
        self.length = node
        self.start = start
        self.queue = queue.Queue()
        self.stack = []
        self.visit = set()
    
    def add_vertics(self,From,To):
        self.graph[From-1][To-1] = 1
        self.graph[To-1][From-1] = 1
    
    def Bfs(self):
        print(self.start,end="")
        self.visit.add(self.start)
        
        for _ in range(self.length): # 처음 스타트랑 연결된 애들 queue에 넣어줌
            if self.graph[self.start-1][_] == 1:
                self.visit.add(_+1)
                self.queue.put(_+1)
        
        while not self.queue.empty(): # 큐에 넣을 때 방문한 것인지 확인, 큐에서 뺄 때 print 
            now = self.queue.get()
            print(" %d" %now,end="")
            for _ in range(self.length):
                if self.graph[now-1][_] == 1 and _+1 not in self.visit:
                    self.visit.add(_+1)
                    self.queue.put(_+1)
        
        self.visit = set()
    
    def Dfs(self):
        print(self.start,end="")
        self.stack.append(self.start)
        self.visit.add(self.start)
        
        while self.stack != []:
            top = self.stack[-1]
            pop_cnt = 1
            for _ in range(self.length):
                if self.graph[top-1][_] == 1 and _+1 not in self.visit:
                    print(" %d" %(_+1),end="")
                    self.stack.append(_+1)
                    self.visit.add(_+1)
                    pop_cnt = 0
                    break
            if pop_cnt: # 스택 최상위 노드에서 방문 안 한 애가 없을 때
                self.stack.pop()
        
        self.visit=set()
            
def main():
    N,M,V = map(int,sys.stdin.readline().split())
    g = Graph(N,V)
    for _ in range(M):
        a,b = map(int,sys.stdin.readline().split())
        g.add_vertics(a,b)
    g.Dfs()
    print()
    g.Bfs()
    
    
if __name__ == "__main__":
    main()
