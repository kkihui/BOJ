import sys

count = 0
N = int(sys.stdin.readline())
numli = list(range(1,N+1))
inputli = list(map(int,sys.stdin.readline().split()))
if inputli == numli[::-1]:
    print(-1)
else:
    for _ in range(N-1):
        numli.remove(inputli[_])
        if inputli[_+1:] == numli[::-1]:
            num = 100000
            for i in range(len(numli)):
                if numli[i] > inputli[_]:
                    if numli[i] < num:
                        num = numli[i]
                        index = i
            numli[index] = inputli[_]
            inputli[_] = num
            numli.sort()
            inputli[_+1:] = numli
            break
    print(*inputli)