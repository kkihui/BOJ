import sys

n = int(sys.stdin.readline())
coorli = [[0]*2 for _ in range(n)]
for _ in range(n):
    coorli[_] = list(map(int,sys.stdin.readline().split()))
coorli.sort(key=lambda x:(x[1],x[0]))
for _ in coorli:
    print(*_)