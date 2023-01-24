def find(a,b): #a층 b호에 사는 사람 찾는 함수
    floor = list(range(1,b+1)) # 0층 1호~0층 N호 까지의 사람 수 배열
    apart = list([0]*b for _ in range(a+1)) # 0층~a층
    apart[0] = floor
    # print(apart) # apart 초기 값 잘 나오나 확인용
    for _ in range(1,a+1):
        for i in range(b):
            for j in range(i+1):
                apart[_][i] += apart[_-1][j]
    # print(apart) # apart 결과 잘 나오나 확인용
             
    
    return apart[a][b-1] #a층 b호에 사는 사람 수

T = int(input())
for i in range(T): #Test case 개수만큼 반복
    k = int(input())
    n = int(input())
    print(find(k,n))