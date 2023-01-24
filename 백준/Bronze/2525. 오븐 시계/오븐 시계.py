A,B = map(int,input().split())
C = int(input())


if (B+C >=60): # 60분을 넘어갈 경우
    A = A + (B+C)//60
    B = (B+C)%60
    
    if (A >= 24): # 그 중에서 A가 24시를 넘어갈 경우
        A = A-24 
    
else:
    B = B + C

print('%d %d'%(A,B))