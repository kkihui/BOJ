import sys
import queue

class Graph:
    def __init__(self,row,col):
        self.map = [[0]*col for _ in range(row)]
        self.visited = set((0,0))
        self.queue = queue.Queue()
    
    def bfs(self,row,col):
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        self.queue.put((0,0,1))
        
        while not self.queue.empty():
            now = self.queue.get()
            r = now[0]
            c = now[1]
            
            if r == row-1 and c == col-1: #목적지 도착
                return now[2]
            
            for k in range(4): # 4방향 탐색
                nr = r+dr[k]
                nc = c+dc[k]
                if 0<=nr<row and 0<=nc<col and (nr,nc) not in self.visited: # 이동 방향이 범위 내에 있고, 아직 탐색 안 했으면
                    if self.map[nr][nc] == '1': # 뚫려있으면 queue에 추가
                        self.visited.add((nr,nc))
                        self.queue.put((nr,nc,now[2]+1))
                        
def main():
    N,M = map(int,sys.stdin.readline().split())
    g = Graph(N,M)
    
    for _ in range(N):
        g.map[_] = list(sys.stdin.readline().rstrip())
        
    ans = g.bfs(N,M)
    print(ans)
    
if __name__ == "__main__":
    main()