import sys
import queue

class Graph:
    def __init__(self,person):
        self.graph = [[0]*person for _ in range(person)]
    
    def add_edge(self,a,b):
        self.graph[a-1][b-1] = 1
        self.graph[b-1][a-1] = 1
        
    def bfs(self,num,start):
        bfs_queue = queue.Queue()
        bfs_queue.put((start,1))
        visit = set()
        visit.add(start)
        ans = 0
        
        while not bfs_queue.empty():
            now,length = bfs_queue.get()
            for _ in range(num):
                if self.graph[now-1][_] == 1 and _+1 not in visit and _ != now-1: # 연결됨 + 아직 안 감 + 본인 아님
                    bfs_queue.put((_+1,length+1))
                    visit.add(_+1)
                    ans += length

        return ans

def main():
    N,M = map(int,sys.stdin.readline().split())
    ans,kbmin = 0,10000
    g = Graph(N)
    
    for _ in range(M):
        a,b = map(int,sys.stdin.readline().split())
        g.add_edge(a,b)
    
    for _ in range(1,N+1):
        kbnum = g.bfs(N,_)
        if kbnum < kbmin:
            kbmin = kbnum
            ans = _
    
    print(ans)
            

if __name__ == '__main__':
    main()