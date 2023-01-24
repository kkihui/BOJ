import sys

K = int(sys.stdin.readline())
numli = []
for _ in range(K):
    a = int(sys.stdin.readline())
    if a == 0:
        numli.pop()
    else:
        numli.append(a)
print(sum(numli))