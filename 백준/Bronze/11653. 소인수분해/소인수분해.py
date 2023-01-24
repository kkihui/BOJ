n = int(input())

if n==1:
    pass
else:
    while n != 1: # n=1 되면 끝
        for _ in range(2,n+1): # 2부터 시작해서 n까지 나눠 떨어지는 수 중 제일 작은거 찾으면 됨
            if n%_ == 0:
                print(_)
                n = n//_
                break