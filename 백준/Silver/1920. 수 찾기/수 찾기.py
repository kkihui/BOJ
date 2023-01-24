import sys

N = int(sys.stdin.readline())
nli = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
mli = list(map(int,sys.stdin.readline().split()))
nli.sort()

for _ in mli:
    init = 0
    final = N-1
    while init <= final:
        mid = (init+final)//2
        if nli[mid] == _:
            print(1)
            break
        elif nli[mid] < _:
            init = mid+1
        else:
            final = mid-1
    if nli[mid] != _:
        print(0)