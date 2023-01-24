import sys

dic = {}
m,n = map(int,sys.stdin.readline().split())
for _ in range(m):
    id,bibun = map(str,sys.stdin.readline().split())
    dic[id] = bibun
for _ in range(n):
    find = sys.stdin.readline().rstrip()
    print(dic[find])