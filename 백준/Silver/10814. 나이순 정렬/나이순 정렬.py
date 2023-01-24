import sys

N = int(sys.stdin.readline())
ali = [[0,0] for _ in range(N)]

for _ in range(N):
    ali[_][0],ali[_][1] = map(str,sys.stdin.readline().split())

ali.sort(key = lambda x: int(x[0])) # 숫자 기준으로 정렬
for _ in range(N): # 2차원 배열 싹 출력
    print(ali[_][0]+' '+ali[_][1])