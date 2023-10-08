import sys
import queue

sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self,row,col):
        self.map = [[0]*col for _ in range(row)]
        self.ans = [['e']*col for _ in range(row)]
        self.graph = [[[] for i in range (col)] for _ in range(row)]
        self.object = [0,0]
        self.visited = [[0]*col for _ in range(row)]
        self.queue = queue.Queue()
    
    def map2graph(self):
        row = len(self.map)
        col = len(self.map[0])
        
        for i in range(row):
            for j in range(col):
                if self.map[i][j] == 2:
                    self.map[i][j] = 1
                    self.object = [i,j]
        
        for i in range(row):
            for j in range(col):
                if self.map[i][j] == 0:
                    self.ans[i][j] = 0
                else:
                    if i == 0: # 아래만 체크
                        if self.map[i+1][j] == 1:
                            self.add_edge(i,j,i+1,j)
                    elif i == row-1: # 위만 체크
                        if self.map[i-1][j] == 1:
                            self.add_edge(i,j,i-1,j)
                    else: # 위아래 체크
                        if self.map[i+1][j] == 1:
                            self.add_edge(i,j,i+1,j)
                        if self.map[i-1][j] == 1:
                            self.add_edge(i,j,i-1,j)
                            
                    if j == 0: # 오른쪽만 체크
                        if self.map[i][j+1] == 1:
                            self.add_edge(i,j,i,j+1)
                    elif j == col-1: # 왼쪽만 체크
                        if self.map[i][j-1] == 1:
                            self.add_edge(i,j,i,j-1)
                    else: # 좌우 체크
                        if self.map[i][j+1] == 1:
                            self.add_edge(i,j,i,j+1)
                        if self.map[i][j-1] == 1:
                            self.add_edge(i,j,i,j-1)                
                        
    def add_edge(self,a,b,c,d):
        self.graph[a][b].append([c,d])
        
    def bfs(self,row,col): # 비재귀적으로 bfs 구현
        for _ in self.graph[row][col]:
                self.queue.put([_[0],_[1],0])
        self.visited[row][col] = 1
        self.ans[row][col] = 0
    
        while not self.queue.empty(): # 큐가 빌 때까지 반복
            now = self.queue.get()
            nrow,ncol,nlen = now[0],now[1],now[2]+1
            
            if self.visited[nrow][ncol] != 1: # 방문한 적 있으면 작동X
                self.visited[nrow][ncol] = 1
                self.ans[nrow][ncol] = nlen
                for _ in self.graph[nrow][ncol]:
                    self.queue.put([_[0],_[1],nlen])
                        
    def clean_outsider(self,row,col):
         for i in range(row):
            for j in range(col):
                if self.ans[i][j] == 'e':
                    self.ans[i][j] = -1
                
def main():
    N,M = map(int,sys.stdin.readline().split())
    g = Graph(N,M)
    
    for _ in range(N):
        g.map[_] = list(map(int,sys.stdin.readline().split()))
    
    g.map2graph()
    g.bfs(g.object[0],g.object[1])
    g.clean_outsider(N,M)
    
    for _ in range(N):
        print(*g.ans[_])

if __name__ == "__main__":
    main()