import sys
N = int(sys.stdin.readline())
xli = list(map(int,sys.stdin.readline().split()))
xset = set(xli) # set으로 중복 제거
newxli = list(xset)
xdic = {}
newxli.sort()
for _ in range(len(newxli)):
    xdic[newxli[_]] = _
for _ in range(N):
    xli[_] = xdic.get(xli[_])
print(*xli)