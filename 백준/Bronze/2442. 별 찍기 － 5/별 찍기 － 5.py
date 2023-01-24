N = int(input())
nli = []
for _ in range(1,N+1):
    s = str(' '*(N-_) +'*'*(2*_-1))
    nli.append(s)
for _ in nli:
    print(_)