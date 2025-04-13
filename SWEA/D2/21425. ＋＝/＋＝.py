T = int(input())

for t in range(T):
    x,y,n = map(int,input().split())
    cnt = 0
    
    while max(x,y) <= n:
        if x<=y: x += y
        else: y += x
        cnt += 1
    print(cnt)