import sys
N = int(sys.stdin.readline().rstrip())
paper = [[0]*100 for _ in range(100)] #0으로 채운 100*100 2차원 배열 만들기
sum = 0
for _ in range(N): #주어진 수의 넓이만큼 1로 바꿔주기 
    x,y = map(int,sys.stdin.readline().split())
    for j in range(x-1,x+9):
        for k in range(y-1,y+9):
            paper[j][k] = 1
for _ in range(100):
    sum += paper[_].count(1) # 1갯수 세기 = 넓이 구하기
print(sum)