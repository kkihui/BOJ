import sys
import copy
K = int(sys.stdin.readline())
building = list(map(int,sys.stdin.readline().split()))
tree = [0]*(2**K)
i = 2**(K-1)
j = 0
visit = {}

for _ in range(1,2**K):
    visit[_] = False

while j<(len(building)):
    if i*2 >= 2**K: # 제일 아래의 level은 자식 없으므로 탐색하고 올라감
        tree[i] = building[j]
        visit[i] = True
        i = i//2
        j += 1
    else:
        if visit[i*2] == False: #왼쪽 자식 아직 안 갔으면 이동
            i *= 2
        else: # 왼쪽 자식 갔으면
            if visit[i] == False: # 본인 탐색 안 했으면 함
                tree[i] = building[j]
                visit[i] = True
                j += 1
            else:
                if visit[i*2+1] == False: #왼쪽 자식과 본인은 갔는데 오른쪽 자식 안 갔으면
                    i = i*2+1
                else: # 모두 갔으면 부모 노드로
                    i = i//2

for _ in range(1,K+1):
    ans = tree[(2**(_-1)):(2**_)]
    print(*ans)