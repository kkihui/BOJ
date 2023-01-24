import sys
N = int(sys.stdin.readline())
for _ in range(N):
    M = int(sys.stdin.readline())
    mli = []
    result = 0
    for i in range(M):
        mli.append(list(map(int,sys.stdin.readline().split())))
    kda = list(map(int,sys.stdin.readline().split()))
    for i in mli:
        sum = kda[0]*i[0] - kda[1]*i[1] + kda[2]*i[2]
        if sum >0:
            result += sum
    print(result)