import sys

fibonacci = [[0,0] for _ in range(41)]
fibonacci[0][0] = 1
fibonacci[1][1] = 1

for _ in range(2,41):
    fibonacci[_][0] = fibonacci[_-1][0] + fibonacci[_-2][0]
    fibonacci[_][1] = fibonacci[_-1][1] + fibonacci[_-2][1]   
    
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(*fibonacci[n])