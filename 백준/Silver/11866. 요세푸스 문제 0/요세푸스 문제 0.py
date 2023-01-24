import sys

N,K= map(int,sys.stdin.readline().split())
pli = [_ for _ in range(1,N+1)]
resli = []


for _ in range(N): # 정렬하면서 제거해서 요세푸스 순열 만듦
    resli.append(pli[K%len(pli)-1])
    pli = pli[K%len(pli)-1:]+pli[:K%len(pli)-1]
    del(pli[0])

print('<', end='')
print(*resli, sep=', ', end='>' )