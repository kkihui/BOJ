import sys
S = set()
M = int(sys.stdin.readline())
for _ in range(M):
    st = sys.stdin.readline().rstrip()
    if 'add' in st:
        S.add(int(st[4:]))
    if 'remove' in st:
        if int(st[6:]) in S:
            S.remove(int(st[6:]))
    if 'check' in st:
        if int(st[5:]) in S:
            print(1)
        else:
            print(0)
    if 'toggle' in st:
        if int(st[6:]) in S:
            S.remove(int(st[6:]))
        else:
            S.add(int(st[6:]))
    if 'all' in st:
        S = set(range(1,21))
    
    if 'empty' in st:
        S = set()