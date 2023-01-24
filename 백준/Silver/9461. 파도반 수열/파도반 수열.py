import sys

padoban = [1]*101
padoban[0] = 0
for n in range(4,101):
    padoban[n]=padoban[n-5]+padoban[n-1]

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(padoban[N])