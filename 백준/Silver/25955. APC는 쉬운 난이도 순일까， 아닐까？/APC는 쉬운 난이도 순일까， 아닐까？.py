import sys
import copy
dict = {'B':0,'S':1,'G':2,'P':3,'D':4}
res = []
N = int(sys.stdin.readline())
tearli = list(map(str,sys.stdin.readline().split()))
compli = copy.deepcopy(tearli)
compli.sort(key=lambda x:(dict[x[0]],-int(x[1:])))
if tearli == compli:
    print('OK')
else:
    for _ in range(N):
        if tearli[_] != compli[_]:
            res.append(tearli[_])
    res.sort(key=lambda x:(dict[x[0]],-int(x[1:])))
    print('KO')
    print(*res)