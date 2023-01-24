H,M = map(int,input().split())
if (M >=45):
    M = M-45
    print('%d %d'%(H,M))
else:
    if (H != 0): # H가 0아니면 1을 뺌
        H= H-1
        M= M+15 #1시간은 60분 이므로 M+60-45 = M=15
        print('%d %d'%(H,M))
    else: # H가 0이면 23으로 감
        H = 23
        M = M+15
        print('%d %d'%(H,M))