import sys

N,M = map(int,sys.stdin.readline().split())
ball =[_ for _ in range(1,N+1)]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    temp = ball[a-1]
    ball[a-1] = ball[b-1]
    ball[b-1] = temp
    
print(*ball)