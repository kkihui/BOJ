import sys
N = int(sys.stdin.readline())
nli = []
ansli = [0]*N
for _ in range(N):
    nli.append(int(sys.stdin.readline()))

if nli[0] != 1:
    print(-1)
    exit()
    
for _ in range(1,N):
    if nli[_] - nli[_-1] > 1:
        print(-1)
        exit()
start = 0
end = 1
while start != N:
    if end == N:
        start += 1
        end = start+1
    else:
        if nli[start] == nli[end]:
            start += 1
            end = start+1
        elif nli[start] == nli[end]-1:
            ansli[start] += 1
            end += 1
        else:
            end += 1

for _ in ansli:
    print(_)