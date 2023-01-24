import sys

N = int(sys.stdin.readline())
ali = [0]*10000
for _ in range(N):
    a = int(sys.stdin.readline())
    ali[a-1] += 1
for _ in range(10000):
    for i in range(ali[_]):
        print(_+1)