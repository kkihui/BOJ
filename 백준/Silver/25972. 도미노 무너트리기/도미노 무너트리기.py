import sys
N=int(sys.stdin.readline())
domino = [0]*N
doneli = [0]
count = 0
for _ in range(N):
    domino[_] = list(map(int,sys.stdin.readline().split()))
domino.sort()

for _ in range(N-1):
    if domino[_] != doneli[-1]:
        doneli.append(domino[_])
        count += 1
        if domino[_][0] + domino[_][1] >= domino[_+1][0]:
            doneli.append(domino[_+1])
        
    else:
        if domino[_][0] + domino[_][1] >= domino[_+1][0]:
            doneli.append(domino[_+1])
if domino[N-1] != doneli[-1]:
    count += 1
print(count)