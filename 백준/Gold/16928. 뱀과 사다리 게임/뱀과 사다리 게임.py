import sys
from collections import deque

class Graph:
    def __init__(self):
        self.board = [0 for _ in range(101)]
        self.deque = deque()
        self.visit = [100 for _ in range(101)] # visit에 최소값 기록
        
    def bfs(self): # 비재귀적으로 bfs 구현
        self.deque.append((1,0))
        ans = 100
        while not self.deque == deque(): # 덱이 빌 때까지 반복
            now,cnt = self.deque.popleft()
            teleport = self.board[now]
            if teleport != 0: # 사다리나 뱀은 무조건 타야함.
                if self.visit[teleport]  > cnt: # 이번 방문이 최소일 때만 넣어줌.
                    self.deque.appendleft((teleport,cnt)) # 주사위 안 굴리니까 우선순위를 줌
                    self.visit[teleport] = cnt

            else:
                for dice in range(1,7): # 주사위 굴려서 나오는 수 추가
                    new = now + dice
                    if new <= 100 and self.visit[new] > cnt+1: # 이번 방문이 최소일 때만 넣어줌.
                        self.deque.append((new,cnt+1))
                        self.visit[new] = cnt+1
                        
                        if new == 100: # 마지막에는 무조건 주사위로 100에 들어옴. 여러 경우 중 최소 구하기
                            ans = min(ans,cnt+1)
        return ans
                
def main():
    g = Graph()
    N,M = map(int,sys.stdin.readline().split())
    
    for i in range(N+M):
        a,b = map(int,sys.stdin.readline().split())
        g.board[a] = b
        
    a = g.bfs()
    print(a)
    
if __name__ == "__main__":
    main()