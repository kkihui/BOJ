import sys

N,M = map(int,sys.stdin.readline().split())
baguni =[_ for _ in range(1,N+1)]

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    temp = baguni[i-1:j]
    baguni[i-1:j] = temp[::-1]

print(*baguni)