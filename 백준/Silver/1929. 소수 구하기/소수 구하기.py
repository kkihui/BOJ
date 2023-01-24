import math

M,N = map(int,input().split())
numlist = list(range(M,N+1))
end = False
i = M

while end ==False:
    if i == 1: #1부터 시작하면 바로 2로 넘김
        i = 2
        
    dec = True
    
    for _ in range(2,int(math.sqrt(i))+1): #2~root(i)//1 + 1의 수까지 다 나눠봄
        if i%_ == 0: # 나눠 떨어지면 소수X
            dec = False
            break
        
    if dec == True: #decimal이 끝까지 true라면
        print(i)
    
    if i == N: #i가 N에 도달하면 끝
        end = True
    i += 1