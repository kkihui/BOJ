import sys
import itertools

count = 0
N = int(sys.stdin.readline())
cake = list(map(int,sys.stdin.readline().split()))
caseli = []
for _ in range(N):
    cake[_] = 1 * (100/cake[_])

for _ in range(1,N+1):
    caseli.extend(list(itertools.combinations(cake,_))) 

if (sum(cake)) < 99:
    print(0)
    exit()

for _ in caseli:
    if 99 <= sum(_) <= 101:
        count += 1
print(count)