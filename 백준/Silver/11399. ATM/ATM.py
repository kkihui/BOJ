import sys

N = int(sys.stdin.readline())
pli = list(map(int,sys.stdin.readline().split()))
pli.sort()
sum = 0
for _ in range(N):
    sum += pli[_]*(N-_)
print(sum)