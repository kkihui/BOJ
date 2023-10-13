import sys
import queue

class Graph:
    def __init__(self,row,col):
        self.map = [[0]*col for _ in range(row)]
        self.queue = queue.Queue()
        self.visit = set()
    
    def bfs(self,row,col):
        dr,dc = [0,0,-1,1],[1,-1,0,0]
        person = 0
        
        while not self.queue.empty():
            r,c = self.queue.get()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < row and 0 <= nc < col and (nr,nc) not in self.visit:
                    self.visit.add((nr,nc))
                    if self.map[nr][nc] != 'X':
                        self.queue.put((nr,nc))
                        if self.map[nr][nc] == 'P':
                            person += 1
        
        if person == 0:
            person = 'TT'
            
        return person
        
def main():
    N,M = map(int,sys.stdin.readline().split())
    g = Graph(N,M)
    
    for i in range(N):
        row_input = list(sys.stdin.readline().rstrip())
        for j in range(M):
            if row_input[j] == "I":
                g.queue.put((i,j))
                g.visit.add((i,j))
            g.map[i][j] = row_input[j]
    
    ans = g.bfs(N,M)
    print(ans)
    
if __name__ == '__main__':
    main()