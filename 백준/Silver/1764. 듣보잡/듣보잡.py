# 시간 감소 위해 set 사용
import sys

N,M = map(int,sys.stdin.readline().split())
nset = set()
mset = set()
for _ in range(N):
    nset.add(sys.stdin.readline().rstrip())
for _ in range(M):
    mset.add(sys.stdin.readline().rstrip())
resli=list(nset&mset)
resli.sort()
print(len(resli))
for _ in resli:
    print(_)