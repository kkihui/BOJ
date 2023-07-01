# store만 써서 O(1)의 반복으로 빠르게 해줌.
import sys
N = int(sys.stdin.readline())
nli = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mli = list(map(int,sys.stdin.readline().split()))

entli = [0]*20000001# 2천만1개 있으면 -천만 +천만 커버 가능
resli = [0]*M
for _ in nli:
    entli[_] += 1
for _ in range(M):
    resli[_] = entli[Mli[_]]
print(*resli)