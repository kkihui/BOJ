import sys
import copy

n = int(sys.stdin.readline())
paoli = [[0]*2 for _ in range(n)]
rankli = [0]*n
#리스트 받아서 오름차순 정렬
for _ in range(n):
    paoli[_] = list(map(int,sys.stdin.readline().split()))
originalpaoli = copy.deepcopy(paoli)
paoli.sort(key=lambda i : (i[0],i[1]))

# 자기보다 더 높은사람 수로 rank 결정해서 출력
for _ in range(n):
    rank=1
    for i in paoli[_+1:]:
        if paoli[_][0] < i[0] and paoli[_][1] < i[1]:
            rank+=1
    for i in range(n): # 원래값이랑 같은거 다 결정한 등수로 바꿔줌
        if originalpaoli[i] == paoli[_]:
            rankli[i] = rank
    
print(*rankli)