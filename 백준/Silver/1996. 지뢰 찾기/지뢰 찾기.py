import sys

n = int(sys.stdin.readline())
mapli = [[0]*n for _ in range(n)]
ansli = [[0]*n for _ in range(n)]

for _ in range(n):
    k = sys.stdin.readline().rstrip()
    mapli[_] = list(k)

for _ in range(n):
    for i in range(n):
        if mapli[_][i] == '.':
            mapli[_][i] = 0
        else:
            mapli[_][i] = int(mapli[_][i])

for _ in range(n):
    for i in range(n):
        if mapli[_][i] != 0:
            ansli[_][i] = '*'
        else:
            if _ == 0:
                if i == 0:
                    ansli[_][i] = mapli[_][i+1] + mapli[_+1][i] + mapli[_+1][i+1]
                elif i == n-1:
                    ansli[_][i] = mapli[_][i-1] + mapli[_+1][i] + mapli[_+1][i-1]
                else:
                    ansli[_][i] = mapli[_][i-1] + mapli[_+1][i-1] + mapli[_+1][i] + mapli[_+1][i+1] + mapli[_][i+1]
                    
            elif _ == n-1:
                if i == 0:
                    ansli[_][i] = mapli[_][i+1] + mapli[_-1][i] + mapli[_-1][i+1]
                elif i == n-1:
                    ansli[_][i] = mapli[_][i-1] + mapli[_-1][i] + mapli[_-1][i-1]
                else:
                    ansli[_][i] = mapli[_][i-1] + mapli[_-1][i-1] + mapli[_-1][i] + mapli[_-1][i+1] + mapli[_][i+1]
            
            else:
                if i == 0:
                    ansli[_][i] = mapli[_-1][i] + mapli[_-1][i+1] + mapli[_][i+1] + mapli[_+1][i+1] + mapli[_+1][i]
                elif i == n-1:
                    ansli[_][i] = mapli[_-1][i] + mapli[_-1][i-1] + mapli[_][i-1] + mapli[_+1][i-1] + mapli[_+1][i]
                else:
                    ansli[_][i] = mapli[_-1][i-1] + mapli[_-1][i] + mapli[_-1][i+1] + mapli[_][i-1] + mapli[_][i+1] + mapli[_+1][i-1] +  mapli[_+1][i] + mapli[_+1][i+1]
            
            if ansli[_][i] >= 10:
                ansli[_][i] = 'M'

for _ in ansli:
    for i in _:
        print(i,end='')
    print()