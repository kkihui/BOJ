import sys
import queue

class Graph:
    def __init__(self,size):
        self.map = [[0]*size for _ in range(size)]
        self.queue = queue.Queue()
        self.visit = set()
    
    def bfs(self,size):
        dr,dc = [0,0,-1,1],[1,-1,0,0]
        danji,house = [],0
        
        for i in range(size):
            for j in range(size):
                if self.map[i][j] == 1 and (i,j) not in self.visit:
                    self.queue.put((i,j))
                    self.visit.add((i,j))
                
                while not self.queue.empty():
                    r,c = self.queue.get()
                    house += 1
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < size and 0 <= nc < size and (nr,nc) not in self.visit:
                            if self.map[nr][nc] == 1:
                                self.queue.put((nr,nc))
                                self.visit.add((nr,nc))
                
                if house != 0:
                    danji.append(house)
                    house = 0
            
        return danji
        
def main():
    N = int(sys.stdin.readline())
    g = Graph(N)
    
    for i in range(N):
        row_input = list(sys.stdin.readline().rstrip())
        for j in range(N):
            g.map[i][j] = int(row_input[j])
    
    ans = g.bfs(N)
    ans.sort()
    length = len(ans)
    
    if length == 0:
        print(0)
    else:
        print(length)
        for _ in range(length):
            print(ans[_])
    
if __name__ == '__main__':
    main()