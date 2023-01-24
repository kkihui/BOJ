import sys

N = int(sys.stdin.readline().rstrip())
num = 1
K=1

while num<N:
    K +=1
    num += (K-1)*6

print(K)