import sys
import queue

class Graph():
    def __init__(self,num):
        self.pic = [[0]*num for _ in range(num)]
        self.rgblindpic = [[0]*num for _ in range(num)]
        self.grid = []
        self.queue = queue.Queue()
        
    def bfs(self,pic,size):
        grid = self.grid # 튜플 복사해서 재활용 가능하게
        visited = set()
        cnt = 0
        dr = [0,0,-1,1]
        dc = [-1,1,0,0]
        for row,col in grid:
            if (row,col) not in visited:
                visited.add((row,col))
                self.queue.put((row,col))
                cnt += 1 # 새로운 곳에서 탐색 시작 = 구역이 나눠짐
            while not self.queue.empty():
                r,c = self.queue.get()
                for k in range(4): # 4방향에서 같은 색만 탐색
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < size and 0 <= nc < size and (nr,nc) not in visited:
                        if pic[r][c] == pic[nr][nc]:
                            self.queue.put((nr,nc))
                            visited.add((nr,nc))
        return cnt

                   
def main():
    N = int(sys.stdin.readline())
    g = Graph(N)
    
    for i in range(N):
        row_input = list(sys.stdin.readline().rstrip())
        for j in range(N):
            g.pic[i][j] = row_input[j]
            if row_input[j] == 'G':
                g.rgblindpic[i][j] = 'R'
            else:
                g.rgblindpic[i][j] = row_input[j]
            g.grid.append((i,j))
    g.grid = tuple(g.grid)
    a = g.bfs(g.pic,N)
    b = g.bfs(g.rgblindpic,N)
    print(a,b)            

   
if __name__ == "__main__":
    main()