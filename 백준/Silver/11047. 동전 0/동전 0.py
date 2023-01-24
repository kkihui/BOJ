import sys

coinli = []
count = 0
N,K = map(int,sys.stdin.readline().split())
for _ in range(N):
    coinli.append(int(sys.stdin.readline()))

while K>0:
    for _ in coinli[::-1]:
        if K >= _:
            K -=_
            count += 1
            break

print(count)