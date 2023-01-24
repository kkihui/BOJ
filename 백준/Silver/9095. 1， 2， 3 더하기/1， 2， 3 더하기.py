import sys
wayli = [1]*11
wayli[2] = 2
wayli[3] = 4
for _ in range(4,11):
    wayli[_] = wayli[_-1] # 1로 시작 : 1작은 수 만드는 법
    wayli[_] += wayli[_-2] # 2로 시작
    wayli[_] += wayli[_-3] # 3으로 시작
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(wayli[n])
