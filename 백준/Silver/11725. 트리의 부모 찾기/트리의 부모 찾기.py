import sys
import collections

def main():
    N = int(sys.stdin.readline())
    parent = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    queue = collections.deque([1])
    visited = set()
    
    for _ in range(N-1):
        x,y = map(int,sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    
    while queue:
        num = queue.popleft()
        if not num in visited:
            visited.add(num)
            for i in graph[num]:
                if not i in visited:
                    parent[i] = num
                    queue.append(i)
        
    for i in range(2,N+1):
        print(parent[i])
    
if __name__ == "__main__":
    main()
