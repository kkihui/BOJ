import sys

N = int(sys.stdin.readline())
ali = [[0,0] for _ in range(N)]
for _ in range(N):
    ali[_][0],ali[_][1] = map(int,sys.stdin.readline().split())
ali.sort(key = lambda x: (x[0],x[1])) #sort에 key를 통해서 x좌표 기준으로 먼저, 같으면 y좌표로 정렬
for _ in range(N):
    print(ali[_][0],ali[_][1])