import sys

n,m = map(int,sys.stdin.readline().split())
grid = []
x_y = []
for _ in range(n):
    grid.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            x_y.append((i,j))

D = abs(x_y[0][0]-x_y[1][0]) + abs(x_y[0][1]-x_y[1][1])
            
print(D)