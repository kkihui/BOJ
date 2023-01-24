import sys
from traceback import print_list

N,K = map(int,sys.stdin.readline().split())
num = 1
den1 = 1
den2 = 1

for _ in range(1,N+1):
    num *= _
for _ in range(1,K+1):
    den1 *= _
for _ in range(1,N-K+1):
    den2 *= _
print(num//(den1*den2))