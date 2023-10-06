import sys
sys.setrecursionlimit(10000)

class Graph:
    def __init__(self,size):
        self.graph = [[0]*size for _ in range(size)]
        self.linked = []
        self.visited = set()
    
    def add_edge(self,a,b):
        self.graph[a-1][b-1] = 1
        self.graph[b-1][a-1] = 1
    
    def search(self,node):
        self.visited.add(node)
        cnt = 0
        for _ in self.graph[node-1]:
            now = cnt+1
            if _ == 1:
                if now not in self.visited:
                    self.visited.add(now)
                    self.visited.update(self.search(now))
            cnt += 1
        return self.visited
    
    def update_linked(self,search_result):
        if search_result not in self.linked:
            self.linked.append(search_result)
        
    
def main():
    N,M = map(int,sys.stdin.readline().split())
    g = Graph(N)

    for _ in range(M):
        row,col = map(int,sys.stdin.readline().split())
        g.add_edge(row,col)
    
    for _ in range(1,N+1):
        g.update_linked(g.search(_))
        g.visited = set()
   
    print (len(g.linked))

if __name__ == "__main__":
    main()