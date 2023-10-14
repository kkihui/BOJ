import sys
import queue

class Graph:
    def __init__(self,size):
        self.graph = [[0]*size for _ in range(size)]
        self.ans = [[0]*size for _ in range(size)]
        self.size = size
        
    def search(self,init):
        visit = set()
        Queue = queue.Queue()
        for _ in range(self.size):
            if self.graph[init][_] == 1 and _ not in visit:
                Queue.put(_)
                visit.add(_)
        while not Queue.empty():
            now = Queue.get()
            for _ in range(self.size):
                if self.graph[now][_] == 1 and _ not in visit:
                    Queue.put(_)
                    visit.add(_)
        for _ in range(self.size):
            if _ in visit:
                self.ans[init][_] = 1
        
def main():
    N = int(sys.stdin.readline())
    g = Graph(N)
    
    for i in range(N):
        row_input = list(map(int,sys.stdin.readline().split()))
        for j in range(N):
            g.graph[i][j] = row_input[j]
    
    for i in range(N):
        g.search(i)
        print(*g.ans[i])
    
if __name__ == '__main__':
    main()