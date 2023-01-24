import sys

N,M = map(int,sys.stdin.readline().split())
pokemondi = {}
for _ in range(1,N+1):
    pokemondi[_] = sys.stdin.readline().rstrip()
reversdi = {v:k for k,v in pokemondi.items()} # value로 매번 불러오면 O(N) 이지만 key로 찾으면 O(1)임
for _ in range(M):
    q = sys.stdin.readline().rstrip()
    if q.isdigit() == True:
        print(pokemondi[int(q)])
    else:
        print(reversdi[q])