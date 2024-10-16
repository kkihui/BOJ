import collections

dx = (1,-1,0,0)
dy = (0,0,1,-1)

class Graph():
    def __init__(self,map):
        self.map = map
        
    def dfs(self):
        visited = set()
        queue = collections.deque([(0,0,1)])
        height,width = len(self.map), len(self.map[0])
        
        while len(queue) > 0:
            x,y,dist = queue.popleft()
            if not (x,y) in visited:
                visited.add((x,y))
                for i in range(4):
                    new_x = x+dx[i]
                    new_y = y+dy[i]
                    if 0 <= new_x and new_x < height and 0 <= new_y and new_y < width:
                        if not (new_x,new_y) in visited:
                            if self.map[new_x][new_y] == 1:
                                queue.append((new_x,new_y,dist+1))
                        if new_x == height-1 and new_y == width-1:
                            return dist+1
        return -1
    
def solution(maps):
    g = Graph(maps)
    answer = g.dfs()
    return answer