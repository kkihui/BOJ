import sys
import queue

class Graph:
    def __init__(self,row,col,height):
        self.tomato = ([[[0]*col for _ in range(row)] for k in range(height)])
        self.queue = queue.Queue()
        
    # (중요) BFS는 큐에서 뺀 다음이 아닌, 큐에 넣을 때 방문 체크를 해야 중복 방문이 일어나지 않음.    
    def bfs(self,row,col,height): # 비재귀적으로 bfs 구현
        dh = [0,0,0,0,1,-1]
        dr = [0,0,1,-1,0,0]
        dc = [1,-1,0,0,0,0]
        
        while not self.queue.empty(): # 큐가 빌 때까지 반복
            now = self.queue.get()
            for k in range(6): # 6방향 탐색
                nh = now[0] + dh[k]
                nr = now[1] + dr[k]
                nc = now[2] + dc[k]
                if 0<=nr<=row-1 and 0<=nc<=col-1 and 0<=nh<=height-1 and self.tomato[nh][nr][nc] == 0:
                    self.tomato[nh][nr][nc] = 1
                    self.queue.put((nh,nr,nc,now[3]+1))

        return now[3] # 마지막으로 처리한 길이가 최대임.
           
    def Wheter_all(self,row,col,height): # 토마토 다 익을 수 있는지 없는지 판단 (0인지 아닌지로)
        for k in range(height):
            for i in range(row):
                for j in range(col):
                    if self.tomato[k][i][j] == 0:
                        return False
        return True
         
def main():
    M,N,H = map(int,sys.stdin.readline().split())
    g = Graph(N,M,H)
    
    for k in range(H):
        for i in range(N):
            row_input = list(map(int,sys.stdin.readline().split()))
            for j in range(M):
                if row_input[j] == -1: # 빈 곳은 방문했다고 치기
                    g.tomato[k][i][j] = 1
                elif row_input[j] == 1:
                    g.tomato[k][i][j] = 1
                    g.queue.put((k,i,j,0))
        
    if g.queue.empty(): # 익은 사과 없는 경우 예외 처리
        print(-1)
    else:
        day_max = g.bfs(N,M,H)
        
        if g.Wheter_all(N,M,H):
            print(day_max)
        else:
            print(-1)

if __name__ == "__main__":
    main()