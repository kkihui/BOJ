# 더 빠르게 하는 방법
import sys

N,M = map(int,sys.stdin.readline().split())
numli = list(map(int,sys.stdin.readline().split()))
sumli = [0]
sum = 0

for _ in numli:
    sum += _
    sumli.append(sum)

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    print(sumli[j]-sumli[i-1])