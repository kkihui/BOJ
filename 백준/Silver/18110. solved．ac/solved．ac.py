import sys
import math

n = int(sys.stdin.readline())
if n == 0:
    print(0)
    exit()

rank = []
for _ in range(n):
    rank.append(int(sys.stdin.readline()))
rank.sort()
elim = math.floor(n*0.15+0.5)

if elim == 0:
    mean = sum(rank)/(len(rank))
else:
    mean = sum(rank[elim:-elim])/(len(rank[elim:-elim]))

mean = math.floor(mean+0.5)

print(mean)