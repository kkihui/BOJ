t = int(input())
for _ in range(t):
    num = int(input())
    coin = [0,0,0,0]
    
    # 25센트
    n = num // 25
    coin[0] = n
    num -= n*25
    
    # 10 센트
    n = num // 10
    coin[1] = n
    num -= n*10
    
    # 5 센트
    n = num // 5
    coin[2] = n
    num -= n*5
    
    # 1 센트
    coin[3] = num
    
    print(*coin)