import sys

N,M,B = map(int,sys.stdin.readline().split())
homeli,tli = [],[]

for _ in range(N): # 주어진 집터를 1차원 배열로 만듦
    homeli.extend(map(int,sys.stdin.readline().split()))

soil = sum(homeli)+B # 사용가능한 block 개수
hmax = min(soil//(M*N),max(homeli))
hmin = max(0,min(homeli))

for _ in range(hmax,hmin-1,-1): # 2진탐색으로하기에는 경향성이 애매해서 선형탐색으로 함
    t=0
    for i in homeli: # 만들 높이 - 현재 높이 하면 작업량이 나옴
        if _-i >=0: # 블럭 추가
            t += _-i
        else: # 블럭 제거
            t += (_-i) *(-2)
    tli.append(t)

res_t = min(tli)
res_h = hmax-tli.index(min(tli)) # 최소 시간이면서, list 제일 왼쪽에 있는 index 찾음.hmax부터 시작했기 때문에 가장 높은 높이가 찾아짐 배열의 0 값인 hmax에서 빼준다.
print(res_t,res_h)