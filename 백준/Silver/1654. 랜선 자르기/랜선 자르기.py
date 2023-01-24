import sys
K,N = map(int,sys.stdin.readline().split())
lanli = []

for _ in range(K):
    lanli.append(int(sys.stdin.readline()))

max = sum(lanli)//N
min = 1

while min <= max: # 이분 탐색으로 갯수 맞는 범위 찾고
    mid = (max+min)//2
    sum = 0
    for _ in lanli:
        sum += _//mid
    if sum == N:
        break
    elif sum > N:
        min = mid+1
    else:
        max = mid-1

del sum
nali = [[0]*2 for _ in range(K)]
minval = sum(lanli)//N

for _ in range(len(lanli)): # 주어진 mid로 나눈 몫과 나머지를 2차원 리스트로 만듦
    nali[_][0] = lanli[_] // mid
    nali[_][1] = lanli[_] % mid
for _ in nali:
    if _[0] != 0: # 몫이 0인 랜선은 신경 X(냅두면 오류남)
        if _[1]//_[0] < minval: # 그 몫과 나머지로 개수 만족하는 최댓값 찾기
            minval = _[1]//_[0]

a = mid+minval
while True: # 1,2칸 보정
    sum=0
    for _ in lanli:
        sum += _//a
    if sum < N:
        break
    a += 1

print(a-1)