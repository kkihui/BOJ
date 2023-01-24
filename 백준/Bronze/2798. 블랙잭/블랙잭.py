import sys

N,M = map(int,sys.stdin.readline().split())
cardli = list(map(int,sys.stdin.readline().split()))
cardli.sort()
sumli =[]
resli =[]

for _ in range(N): # 카드 3개의 합 찾기, 최대 100*99*98=970200번 연산 
    a = cardli[_]
    cardli.remove(a)
    for i in range(N-1):
        b = cardli[i]
        cardli.remove(b) 
        for k in range(N-2):
            c = cardli[k]
            sumli.append(a+b+c)
        cardli.append(b)
        cardli.sort()
    cardli.append(a)
    cardli.sort()
sumli.sort()

for _ in sumli: # 선형탐색으로 찾기
    if _ <= M:
        resli.append(_)
    else: # 커지면 바로 종료
        break
        
print(max(resli))