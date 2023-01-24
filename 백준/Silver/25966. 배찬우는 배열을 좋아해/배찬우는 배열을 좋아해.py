import sys
N,M,q = map(int,sys.stdin.readline().split())

li2 = [[0]*M for _ in range(N)]
for _ in range(N):
    li2[_] = list(map(int,sys.stdin.readline().split()))

for _ in range(q):
    quary = list(map(int,sys.stdin.readline().split()))
    i = quary[1]
    j = quary[2]
    if quary[0] == 0:
        k = quary[3]
        li2[i][j] = k
         
    else:
        li2.append(li2[i])
        li2[i] = li2[j]
        li2[j] = li2.pop()

for _ in li2:
    print(*_)