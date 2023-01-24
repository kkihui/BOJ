N = int(input())
nli = []
for _ in range(N,0,-1):
    s = str(' '*(N-_) +'*'*_)
    nli.append(s)
for _ in nli:
    print(_)