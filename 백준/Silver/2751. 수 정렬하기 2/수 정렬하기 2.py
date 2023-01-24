import sys

N = int(sys.stdin.readline())
ali = [int(sys.stdin.readline()) for _ in range(N)]
ali.sort()
for _ in range(N):
    print(ali[_])